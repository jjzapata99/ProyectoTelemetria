# ProyectoTelemetria - Control de Aire Acondicionado dentro de un Data Center

En este repositorio se encuentran los archivos .py necesarios para el control de temperatura a nivel básico dentro de un DataCenter.
Especificando los archivos presentes en este repositorio se tiene el archivo ping.py
# Ping.py

En dicho archivo se presenta el codigo para poder realizar el sensado del número de servidores activos actualmente en el datacenter.
Inicialmente se creará la conexión con la base de datos, especificando la ip del servidor, puerto, usuario, contraseña y la base de datos a utilizar.
Para este proyecto se utilizo el broadlink con la finalidad de controlar el aire acondicionado, este dispositivo es capaz de aprender configuraciones presentes en un control remoto, esta funcion fue utiliza al invocar el comando 
