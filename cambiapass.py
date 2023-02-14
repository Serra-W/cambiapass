#!/usr/bin/python


################################################################
# Programa para cambiar ips de forma masiva en equipos linux   #
#              Funciona en equipos Windows/Linux               #
#                       Serra-W 1.0v                           #
################################################################

import os                                                      #Libreria permite usar comando en el sistema
from getpass import getpass                                    #Libreria para poner la contraseña de forma segura.
import paramiko                                                #Libreria SSH.

#PARAMIKO------------------------------------------------
ssh = paramiko.SSHClient()                                     #Variable con la funcion de cliente SSH.
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())      #Guarda la key que se genera en la primera conexion ssh.

#USUARIO-------------------------------------------------
usuario=input("Inserte el nombre de usuario: ")                #Nombre de usuario del equipo remoto

#CONTRASEÑA----------------------------------------------
contra=str(getpass("Contraseña de "+usuario+": "))             #Contraseña ACTUAL del sistema que se va a cambiar.
nuevaspass=str(getpass("Nueva contraseña: "))                  #Nueva Contraseña.
vnuevapass=str(getpass("Introduzca de nuevo la contraseña: ")) #Variable para validar que la contraseña es la correcta.
if nuevaspass != vnuevapass:                                   #If para que no pongas mal la contraseña.
    raise ValueError("La nueva contraseña no coinciden...")

#Abrir Archivo de Ips------------------------------------
try:
    patharchivo=input("Introduce la ruta del archivo de ips: ")#Variable con la ruta del fichero de ips
    archivo=open(str(patharchivo),"r")                         #Lectura Archivo con IPs. Solo una ip en cada linea.
except:
    print("No se encontro el archivo de ips...")
registroruta='registro.txt'                                    #Ruta del archivo registro en caso de no poder conectarse con el equipo.


#COMANDO-------------------------------------------------
comando= "echo '"+usuario+":"+nuevaspass+"' | sudo chpasswd"  #Comando para cambiar la contraseña.


#Script----------------------------------------------------------------------
for ip in archivo.readlines():                                                      #Bucle para leer linea a linea el fichero de las ip.
    try:                                                                            #Intenta la conexion por ssh con el equipo.
        ssh.connect(ip, 22, username=usuario, password=contra ,timeout=4)           #Conexión con el equipo.
        stdin, stdout, stderr = ssh.exec_command(comando, get_pty=True)             #Ejecución del comando en el equipo remoto
        stdin.write(contra+'\n')                                                    #Inserta la contraseña de sudo.
        stdin.flush()                                                               #Borra la entrada input.
        if stderr.channel.recv_exit_status() != 0:                                  #Si stderr(Errores) no es 0.
            print(f"Error: {stderr.read()}")                                        #Devuelve un error al ejecutar el comando.
        else:                                                                       #Si stderr(Errores) es 0.
            print(f"{stdin.readlines()}")                                           #Devuelve el resultado del comando en caso de que no sea un error.
        ssh.close()                                                                 #Cierra la conexión ssh.
    except:                                                                         #Si no logra conectar con el equipo por ssh.
        if not os.path.exists(registroruta):                                        
            registro=open('registro.txt', 'x')                                      #Genera un archivo llamado registro (En caso de que no exista) en el mismo sitio donde este el script.
            registro.write(str(ip))                                                 #Escribe la ip del equipo que no puede conectar en registro.
            registro.close()                                                        #Cierra el fichero registro.
        else:
            registro=open('registro.txt', 'a')
            registro.write("\n"+str(ip))                                            #Escribe la ip del equipo que no puede conectar en registro.
            registro.close()                                                        #Cierra el fichero registro.
#----------------------------------------------------------------------------