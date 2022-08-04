import Adafruit_DHT # libreria del sensor
import time 
import MySQLdb #libreria de base de dato
from datetime import datetime
#Conexion para la base de datos
db=MySQLdb.connect(host="200.126.14.231",user="root",passwd="telemetria",port=4097, database="tempDataCenter")
#cursor para la peticiones de la base de datos
cur= db.cursor()
#varible del tipo de sensor y el pin a utilizar
SENSOR_DTH = Adafruit_DHT.DHT11
PIN_DHT=17
PIN_DHT_2=4
#bucle de lectura
while True:
    humedad,temperatura=Adafruit_DHT.read(SENSOR_DTH, PIN_DHT)
    humedad_2,temperatura_2=Adafruit_DHT.read(SENSOR_DTH,PIN_DHT_2)
    if temperatura is not None and temperatura_2 is not None:
        print("Temp={0:0.1f}C Hum={1:0.1f}%".format(temperatura,humedad))
        print("Temp2={0:0.1f}C Hum2={1:0.1f}%".format(temperatura_2,humedad_2))
        #Se agrega la lectura a la base de datos
        cur.execute("""INSERT INTO temperatura(temperaturaDC1,temperaturaDC2) VALUES (%s,%s);""",(str(temperatura),str(temperatura_2)))
        db.commit()
    else:
        print("Fallo en la lectura. Revisar el circuito")
    time.sleep(5)#empieza la lectura despues de 5 segundos

