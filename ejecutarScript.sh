#!/bin/bash
echo "script ejecutado - $(date)" >> /home/pi/log-Scripts/log-script.txt
python3 /home/pi/Telematria/sensorTemp.py | python3 /home/pi/Telematria/ping.py
exit
