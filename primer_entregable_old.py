'''Primer entregable ejercicio práctica
Realice al menos una función para cada una de las siguientes operaciones. Cada función deberá recibir como parámetro el directorio en donde trabajará.

1. Genere un listado con los nombres de archivos del directorio.
2. Genere un listado con los nombres de los archivos que comiencen con una letra obtenida al azar (entre todo el alfabeto).
3. Genere una lista con aquellos archivos que han sido modificados en los últimos 30 días y que sean de un tamaño menor a una cantidad (en bytes) ingresada por teclado.
4. Devuelva el tamaño total de los archivos de imagen (.png, .jpg, .bmp, .jpeg).
5. Devuelva  una lista con los nombres de los archivos del directorio ordenados por tamaño.
6. Modifique los incisos anteriores para que utilicen lambda (en caso de ser necesario).'''

import random
import string

from os import system, name, path, stat

from time import sleep 
from datetime import timedelta, datetime
def clear():
	'''Funcion para limpiar la consola. sacada de (https://www.geeksforgeeks.org/clear-screen-python/) '''

	if name == 'nt':
		_ = system('cls') 
	else: 
		_ = system('clear') 

from os import listdir, getcwd
from os.path import isfile, join, getatime, getsize


def imprimir(lista):
	formato_col='{:<20}|'
	print('-'*65)
	print(formato_col.format('Nombre de archivo'))
	print('-'*65)
	


def listarArchivos(ruta):
	for x in listdir(ruta):
		if isfile(x):
			print(x)

def generar_lista_azar(ruta):
	ch=random.choice(string.ascii_letters)
	lista=list(filter(lambda x: x.startswith(ch) and isfile(x), listdir(ruta)))
	print(ch)
	if lista != []:
		for x in lista:
			print(x)
	else : print('No existen archivos que comiencen con ',ch)

def lista_restringida(ruta = getcwd(), dias = 30):
	
	s = int(input('Ingrese el límite de tamaño (en bytes) que los archivos no deben superar:'))
	t = datetime.now().date() - timedelta(days=dias)
	
	lista = list(filter(lambda x: isfile(x) and datetime.fromtimestamp(getatime(x)).date() > t and getsize(x)<s , listdir(ruta)))
	if lista != []:
		for x in lista:
			print(x)
	else : print('No existen archivos con esa fecha y tamaño')


menu ='''\n
*+       MENU       +* \n
\n
1. Listado con los nombres de archivos del directorio. \n
2. Genere un listado con los nombres de los archivos que comiencen con una letra obtenida al azar (entre todo el alfabeto). \n
3. Genere una lista con aquellos archivos que han sido modificados en los últimos 30 días y que sean de un tamaño menor a una cantidad (en bytes) ingresada por teclado. \n
4. Devuelva el tamaño total de los archivos de imagen (.png, .jpg, .bmp, .jpeg). \n
5. Devuelva  una lista con los nombres de los archivos del directorio ordenados por tamaño. \n
6. Modifique los incisos anteriores para que utilicen lambda (en caso de ser necesario). \n
x. Salir. \n
'''
opc = input (menu+'Ingrese opción: ')
while opc not in ('1','2','3','4','5','6','x','X'): #si ingresa un no valido, vuelve a preguntar (y a dibujar)
	clear()
	opc = input (menu + 'Opción no válida, intente nuevamente: ')

if opc == '1' :
	clear()
	ruta = input('Ingrese ruta (enter para actual): ')
	if ruta == '':
		ruta = getcwd()
	print('Listado con los nombres de archivos del directorio: '+ruta)
	listarArchivos(ruta)
elif opc == '2' :
	clear()
	ruta = input('Ingrese ruta (enter para actual): ')
	if ruta == '':
		ruta = getcwd()
	print('Listado con los nombres de archivos del directorio: '+ruta)
	generar_lista_azar(ruta)
elif opc == '3' :
	lista_restringida()
elif opc == '2' :
	print('1')
elif opc == '5' :
	print('1')
elif opc == '6' :
	print('1')
elif (opc == 'x') or (opc == 'X'):
	print('EXIT')

