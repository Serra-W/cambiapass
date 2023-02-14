# Cambiapass.py
Pequeño script en python para cambiar de forma remota la contraseña en linux en equipos que comparten un mismo usuario. 

LIBRERIAS NECESARIAS:
  -Paramiko

UTILIZACIÓN:
  
  1º- Generar un archivo "TxT" con todas las direcciones ip que se desea cambiar la contraseña. Siendo este archivo de la siguiente forma:
  
  10.0.0.0
  10.0.0.1
  192.168.97.3
  ...
  
  
  
  
  
  2º- Ejecutar el script e insertar la información necesaria en cada input. (Nombre de usuario, contraseña antigua, contraseña nueva e ubicación del archivo de direcciones ip.
