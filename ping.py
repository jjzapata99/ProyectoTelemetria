import platform
import subprocess
import time
import MySQLdb #libreria de base de dato
import broadlink #libreria para el control del aire
#Conexion para la base de datos especificando ip y puerto de la misma
db=MySQLdb.connect(host="200.126.14.231",port=4097,user="root",passwd="telemetria",db="serverEstado")
#cursor para la peticiones de la base de datos
cur= db.cursor()
#Se crea conexion con el broadlink
#En el siguiente comando se especifica la ip del broadlink y posterior autorizacion

device = broadlink.hello('192.168.0.104')

device.auth()

#Lista de servidores
servers=["200.126.14.228","200.126.14.229","200.126.14.230","200.126.14.231","200.126.14.232","200.126.14.233","200.126.14.234","200.126.14.235"]

#Tiempo de espera entre cada ping
n=1

#Comandos aprendidos para setear la temperatura en 17 20 y 24 respectivamente
bajo= b'&\x00\xca\x00\x8c\x92\x107\x10\x14\x0f8\x107\x10\x14\x0f\x14\x107\x10\x13\x10\x14\x0f8\x10\x13\x10\x13\x108\x107\x10\x13\x108\x0f8\x10\x13\x108\x0f8\x107\x107\x108\x107\x10\x13\x108\x10\x13\x10\x13\x10\x14\x0f\x14\x10\x13\x10\x13\x10\x13\x10\x14\x0f\x14\x10\x13\x10\x13\x10\x14\x0f\x14\x10\x13\x107\x108\x0f8\x107\x108\x107\x107\x108\x10\xac\x8f\x92\x0f8\x10\x13\x108\x0f8\x10\x13\x10\x13\x108\x0f\x14\x10\x13\x107\x10\x14\x10\x13\x107\x108\x0f\x14\x107\x107\x10\x14\x107\x107\x108\x107\x107\x108\x10\x13\x107\x10\x14\x0f\x14\x10\x13\x10\x13\x10\x14\x0f\x14\x10\x13\x10\x13\x10\x13\x10\x14\x0f\x14\x10\x13\x10\x13\x10\x14\x0f8\x107\x108\x0f8\x107\x108\x0f8\x107\x10\x00\r\x05'
medio=b'&\x00\xca\x00\x8a\x94\x0e9\x0f\x14\x0e:\x0e9\x0e\x15\x0e\x16\r:\r\x16\x0e\x15\x0e:\r\x16\x0e\x15\x0e9\x0f9\x0e\x15\x0e9\x0e:\x0e\x15\x0e9\x0f9\x0e9\x0e9\x0f9\x0e9\x0e\x15\x0e:\x0e\x15\r\x16\x0e\x15\x0e\x15\x0e\x16\r\x16\x0e\x15\x0e\x15\x0e:\x0e\x15\x0e\x15\x0e\x15\x0e\x16\r\x16\r:\x0e:\r\x16\r:\x0e:\x0e9\r:\x0f8\x0f\xae\x8c\x94\x0f9\x0e\x15\x0e9\x0e:\x0e\x15\x0e\x15\x0e:\r\x16\r\x16\x0e9\x0e\x16\r\x16\r:\x0e9\x0f\x15\r:\x0e9\x0f\x15\r:\x0e9\x0f9\x0e9\x0e9\x0f9\x0e\x15\r:\x0f\x14\x0e\x16\r\x16\r\x16\x0e\x15\x0e\x16\r\x16\r\x16\x0e:\x0e\x15\r\x16\r\x16\x0e\x15\x0e\x16\r:\x0e9\x0f\x14\x0e:\r:\x0f8\x0f9\x0e9\x0f\x00\r\x05'
alto=b'&\x00\xca\x00\x8c\x92\x0f8\x10\x13\x108\x0f8\x10\x13\x10\x14\x0f8\x0f\x14\x10\x13\x108\x0f\x14\x10\x13\x107\x108\x0f\x14\x107\x108\x0f\x14\x107\x108\x0f8\x107\x108\x0f8\x10\x13\x107\x10\x14\x0f\x14\x10\x13\x10\x13\x10\x14\x0f\x14\x10\x13\x108\x0f\x14\x0f\x14\x10\x13\x10\x13\x10\x14\x0f\x14\x107\x10\x13\x108\x107\x107\x108\x107\x107\x10\xad\x8f\x92\x0f8\x10\x13\x107\x108\x0f\x14\x10\x13\x107\x10\x14\x10\x13\x107\x10\x14\x0f\x14\x107\x107\x10\x14\x0f8\x107\x10\x14\x0f8\x107\x107\x108\x107\x107\x10\x14\x107\x10\x13\x10\x14\x0f\x14\x10\x13\x10\x13\x10\x14\x0f\x14\x107\x10\x13\x10\x14\x10\x13\x10\x13\x10\x13\x10\x14\x0f8\x10\x13\x107\x108\x107\x107\x108\x107\x10\x00\r\x05'
#funcion que devuelve un 0 si responde al ping y un 1 en caso contrario
def myping(host):
    parameter= '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', parameter, '1', host]
    response = subprocess.call(command)
    return response

#variables de control
serversI=0
serversF=0
temp=17
tempf=17
while True:

    serv1=myping(servers[0])
    if serv1==0:
        serversI+=1
    time.sleep(n)
    serv2=myping(servers[1])
    if serv2==0:
        serversI+=1
    time.sleep(n)
    serv3=myping(servers[2])
    if serv3==0:
        serversI+=1
    time.sleep(n)
    serv4=myping(servers[3])
    if serv4==0:
        serversI+=1
    time.sleep(n)
    serv5=myping(servers[4])
    if serv5==0:
        serversI+=1
    time.sleep(n)
    serv6=myping(servers[5])
    if serv6==0:
        serversI+=1
    time.sleep(n)
    serv7=myping(servers[6])
    if serv7==0:
        serversI+=1
    time.sleep(n)
    serv8 = myping(servers[7])
    if serv8==0:
        serversI+=1
     #Se agrega la lectura a la base de datos
    cur.execute("""INSERT INTO estadosFinal(srv1,srv2,srv3,srv4,srv5,srv6,srv7, srv8) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);""",(str(serv1),str(serv2),str(serv3),str(serv4),str(serv5),str(serv6),str(serv7),str(serv8)))
    if serversF!=serversI:
        if serversI <= 2:
            if temp==17:
                device.send_data(bajo)
            elif temp==20:
                device.send_data(bajo)
            temp=24
        elif serversI>=3 and serversI<=4:
            if temp==17:
                device.send_data(medio)
            elif temp==24:
                device.send_data(medio)
            temp=20
        elif serversI>4:
            if temp==20:
                device.send_data(alto)
            elif temp==24:
                device.send_data(alto)
            temp=17
    cur.execute("""INSERT INTO temperaturaAire(temperatura) VALUES (%s);""",(str(temp),))
    db.commit()

    tempf=temp
    serversF= serversI
    serversI=0
