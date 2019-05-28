'''Primer entregable ejercicio práctica
Realice al menos una función para cada una de las siguientes operaciones. Cada función deberá recibir como parámetro el directorio en donde trabajará.

1. Genere un listado con los nombres de archivos del directorio.
2. Genere un listado con los nombres de los archivos que comiencen con una letra obtenida al azar (entre todo el alfabeto).
3. Genere una lista con aquellos archivos que han sido modificados en los últimos 30 días y que sean de un tamaño menor a una cantidad (en bytes) ingresada por teclado.
4. Devuelva el tamaño total de los archivos de imagen (.png, .jpg, .bmp, .jpeg).
5. Devuelva  una lista con los nombres de los archivos del directorio ordenados por tamaño.
6. Modifique los incisos anteriores para que utilicen lambda (en caso de ser necesario).'''

import random
from os import system, name 
from time import sleep 
def clear():
	'''Funcion para limpiar la consola. sacada de (https://www.geeksforgeeks.org/clear-screen-python/) '''

	if name == 'nt':
		_ = system('cls') 
	else: 
		_ = system('clear') 

from os import listdir, getcwd
from os.path import isfile, join, getatime


def imprimir(lista):
	formato_col='{:<20}|'
	print('-'*65)
	print(formato_col.format('Nombre de archivo'))
	print('-'*65)
	


def listarArchivos(ruta):
	for x in listdir(ruta):
		if isfile(x):
			print(x)

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

if opc == 1 :
	print('Listado con los nombres de archivos del directorio: ')
	listarArchivos('.')
elif opc == 2 :
	print('1')
elif opc == 3 :
	print('1')
elif opc == 4 :
	print('1')
elif opc == 5 :
	print('1')
elif opc == 6 :
	print('1')
elif (opc == 'x') or (opc == 'X'):
	print('EXIT')

