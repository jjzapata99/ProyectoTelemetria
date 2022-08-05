# ProyectoTelemetria - Control de Aire Acondicionado dentro de un Data Center

En este repositorio se encuentran los archivos .py necesarios para el control de temperatura a nivel básico dentro de un DataCenter.
Especificando los archivos presentes en este repositorio se tiene el archivo ping.py
# Ping.py

En dicho archivo se presenta el codigo para poder realizar el sensado del número de servidores activos actualmente en el datacenter.
Inicialmente se creará la conexión con la base de datos, especificando la ip del servidor, puerto, usuario, contraseña y la base de datos a utilizar.
Para este proyecto se utilizo el broadlink con la finalidad de controlar el aire acondicionado, este dispositivo es capaz de aprender configuraciones presentes en un control remoto, esta funcion fue utiliza al invocar el comando (variable vinculada).enter_learning(), posteriormente con el control del aire se envia el comando y caputara. Finalmente para observar el codigo binario de la configuración del control en ese instante, se usa el comando (variable vinculada).check_data() (este resultado puede ser almacenado en una variable o archivo).
Dentro del archivo .py existen variables que pueden ser modificadas a conveniencia, tales como la lista de servidores y el tiempo de esperan entre cada ping, cuyos nombres de variables son servers y n respectivamente.
Factores a considerar por posibles problemas de funcionamiento son:
  -En cuanto a la base de datos, las credenciales y la dirección donde se aloja la base de datos.
  -El dispositivo broadlink tiende a variar su ip despues de unos días, es recomendable asignarle una ip estatica, este cambio de ip suele traer problemas al momento de ejecutar el codigo ya que no se lograra comunicar con el dispositivo.
#sensorTemp.py
En este codigo se encuentra la lectura y subida de la información obtenida a la base de datos MySQL, el codigo es relativamente sencillo y sin muchas complicaciones, como en el caso anterior posibles complicaciones pueden deberse a la conectibilidad con la base de datos.
