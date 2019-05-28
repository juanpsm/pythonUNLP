f = open('archivo.txt', 'w')
#https://docs.python.org/3.6/library/functions.html#open
'''	Character	Meaning
	'r'	open for reading (default)
	'w'	open for writing, truncating the file first
	'x'	open for exclusive creation, failing if the file already exists
	'a'	open for writing, appending to the end of the file if it exists
	'b'	binary mode
	't'	text mode (default)
	'+'	open a disk file for updating (reading and writing)
	'U'	universal newlines mode (deprecated)
'''
f.write('Hola, \n')
f.write('Mundo!')
f.close()

f = open('archivo.txt', 'r')
print(f.read(4)) #Si cantidad_bytes es <0 o no está, lee hasta fin de archivo.
print(f.read()) #lee desde donde esta parado
f.seek(0)
print(len(f.read()))
f.seek(0)
print(f.readline())
f.close()
#------------------------------- JSON -----------------------------------------------------------
import json
import time
archivo = open("archivoJSON.txt", "w")
datos = [
{'nombre': 'Tony Stark', 'fecha': time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())},
{'nombre': 'Bruce Wayne', 'fecha': time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())}
]
json.dump(datos, archivo)
archivo.close()

import json
archivo = open("archivoJSON.txt", "r")
datos = json.load(archivo)
print(json.dumps(datos, sort_keys=True, indent=4)) #dumps la S es de STRING
archivo.close()

#------------------------------- PICKLE -----------------------------------------------------------
import pickle
import time
archivo = open("archivoPICKLE.txt", "wb")
datos = [
{'nombre': 'Tony Stark', 'fecha': time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())},
{'nombre': 'Bruce Wayne', 'fecha': time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())}]
pickle.dump(datos, archivo)
archivo.close()

archivo = open("archivoPICKLE.txt", "rb")
datos = pickle.load(archivo)

for item in datos:
        for item, valor in item.items():
                print("{}: {}".format(item, valor))
archivo.close()

"seek(desplazamiento, desde_donde)"
# ~ Si el valor desde_donde no está, se asume 0.
# ~ Si el archivo es de texto, solamente se considera desplazar desde el comienzo del archivo, es decir el valor desde_donde es 0.
'''desde_donde = whence
0 (absolute file positioning)				= os.SEEK_SET (DEFAULT)
1 (seek relative to the current position)	= os.SEEK_CUR
2 (seek relative to the file’s end)			= os.SEEK_END
There is no return value.'''

archi = open("archivo.txt","rb")
archi.seek(2, 0)
print(archi.read(4).decode('ASCII'))
archi.seek(-1, 2) #Esto da error si el archivo se abre en modo"r"
print(archi.read().decode('ASCII'))
print(archi.tell()) #retorna la posición actual.
archi.close()

import os
# ~ os.rename('archivo.txt','COPIA.TXT')
# ~ os.remove('COPIA.TXT')
#Directorios: listdir()- mkdir() -chdir() - getcwd() - rmdir()
#Permisos: chmod()- access()

# Algunas funciones útiles: exists(), isdir(), isfile()
import os.path

print(os.path.exists("/home/clau/git/"))
print(os.path.isdir("/home/clau/git/"))
#asd
f = open('archivo.txt','ab')
f.seek(-1, 2)
f.write(b'asd')
f.close()
#no sobreescribe
#para borrar
f = open('archivo.txt', 'r+b')
f.seek(-1, os.SEEK_END)
f.truncate() # si le paso un valor me lo corta a esa cantidad de bytes, por defecto en current pos
f.close()
f = open('archivo.txt', 'r')
print(f.read())
f.close()
