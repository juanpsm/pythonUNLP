# -*- coding: utf-8 -*-
'''Primer entregable ejercicio práctica:
Realice al menos una función para cada una de las siguientes operaciones. Cada función deberá recibir como parámetro el directorio en donde trabajará.

1. Genere un listado con los nombres de archivos del directorio.
2. Genere un listado con los nombres de los archivos que comiencen con una letra obtenida al azar (entre todo el alfabeto).
3. Genere una lista con aquellos archivos que han sido modificados en los últimos 30 días y que sean de un tamaño menor a una cantidad (en bytes) ingresada por teclado.
4. Devuelva el tamaño total de los archivos de imagen (.png, .jpg, .bmp, .jpeg).
5. Devuelva  una lista con los nombres de los archivos del directorio ordenados por tamaño.
6. Modifique los incisos anteriores para que utilicen lambda (en caso de ser necesario).'''
import traceback
def debug(__x):
	'''Devuelve el nombre_var = valor_var, type: tipo_var'''
	print (traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x,', type:',type(__x))

import random
import string

from os import system, name, listdir, getcwd, scandir, fsdecode
from os.path import isfile, getmtime, getsize, join

from time import localtime, strftime, time
from datetime import timedelta
def clear():
	'''Funcion para limpiar la consola. sacada de (https://www.geeksforgeeks.org/clear-screen-python/) '''

	if name == 'nt':
		_ = system('cls') 
	else: 
		_ = system('clear') 

def format_tamaño(T):
	'''Funcion que convierte una cantidad de bytes a KB, MB, GB y TB. Devuelve un string'''
	B='B '
	if T>1024:
		T=round(T/1024,2)
		B='KB'
		if T>1024:
			T=round(T/1024,2)
			B=' MB'
			if T>1024:
				T=round(T/1024,2)
				B='GB'
				if T>1024:
					T=round(T/1024,2)
					B='TB'
	return str(T)+' '+B+' '

def format_fecha_mod(x):
	t=getmtime(x) #devuelve tiempo de modificacion desde epoch
	t=localtime(t) #convierto a tiempo local
	#return str(timedelta(seconds = time() - getmtime(x))) #la resta da los segundos transcurridos desde la mod y timedelta lo convierte a un objeto con campos legibles.
	return strftime("%d %b %Y %H:%M:%S", t) #formateo localtime
	
def imprimir(lista):
	'''Metodo para imprimir la lista de nombres de archivos de manera legible y con detalles (tamaño y fecha_mod'''
	formato_col='{:<25.25}|{:>15}|{:>25}'
	print('-'*99)
	print(formato_col.format('Nombre de archivo','tamaño','fecha modificación'))
	print('-'*100)
	for x in lista:
		print(formato_col.format(x.name , format_tamaño(getsize(x)), format_fecha_mod(x)))

def listarchivos(ruta):	#------------------------------ Punto 1
	'''Este método que recibe un path como parametro y devuelve una lista de todos los nombres de archivo en el directorio'''
	#lista = list(map(lambda x: join(ruta,x) , listdir(ruta)))
	# ~ lista = list(filter(lambda x: isfile(join(ruta,x)), listdir(ruta)))
	lista = list(filter(lambda x: isfile(x), scandir(ruta)))
	return lista

def generar_lista_azar(ruta):	#-------------------------- Punto 2
	'''Este método recibe un path, genera una letra al azar e imprime una lista de los archivos contenidos en el directorio cuyo nombre comienza con esa letra.'''
	ch=random.choice(string.ascii_letters) # string.ascii_letters genera un string con todas las letras unidas, primero minusculas y luego mayuscula.
	lista=list(filter(lambda x: x.name.startswith(ch), listarchivos(ruta))) #filtro los elementos de listarchivos con dos condiciones: que sea archivo y que el nombre comience con la letra.
	print('Letra obtenida al azar: ',ch)
	print()
	if lista != []:
		imprimir(lista)
	else : print('No existen archivos que comiencen con ',ch)

def generar_lista_antiguedad_y_tamaño(ruta, dias = 30):	#-- Punto 3
	'''Este método recibe un path y la cantidad de dias (que por defecto es 30), pregunta una cantidad de bytes e imprime una lista de los archivos contenidos en el directorio 
	que hayan sido modificados en ese rango de dias y que sean de un tamaño menot al tamaño especificado'''
	tam = int(input('Ingrese el límite de tamaño (en bytes) que los archivos no deben superar:')) #necesito que sea entero para poder compararlo con getsize()
	print()
	filtro = list(filter(lambda x: timedelta(seconds = time() - getmtime(x)) < timedelta(days=dias) and getsize(x) < tam, listarchivos(ruta)))
	#timedelta representa un periodo de tiempo en distintos campos (days, hours, seconds, etc)
	# time() - getmtime(x) da la cantidad de segundos que pasaron desde la modificacion del archivo, y con timedelta(seconds =... ) lo converitmos a un objeto que tiene distintos campos para poder compararlo
	ordenada = sorted(filtro, key=lambda x: getmtime(x))
	if ordenada != []:
		imprimir(ordenada)
	else : print('No existen archivos con esa fecha y tamaño')

def tamaño_total_img(ruta):	#------------------------------ Punto 4
	'''Este método recibe un path imprime una lista de los archivos contenidos en el directorio 
	que hayan sido modificados en ese rango de dias y que sean de un tamaño menot al tamaño especificado'''
	def es_imagen(x):
		return x.name.split('.')[-1] in {'png', 'jpg', 'bmp', 'jpeg'} # separo el nombre de archivo con los puntos, me quedo con el ultimo elemento de esa estructura y veo si esta en la lista de extensiones de imágenes
	filtro = list(filter(lambda x: es_imagen(x) , listarchivos(ruta)))
	suma = sum(map(lambda x: getsize(x) , filtro)) #mapea los tamaños en toda la lista de archivos( ya filtrada) y los suma.
	print(format_tamaño(suma))

def lista_por_tamaño (ruta): #----------------------------- Punto 5
	'''Este método recibe un path e imprime una lista, ordenada por tamaño, de los archivos contenidos en el directorio'''
	ordenada = sorted( listarchivos(ruta) , key=lambda x: getsize(x))
	if ordenada != []:
		imprimir(ordenada)
	else : print('No existen archivos en esa ruta.')
	
menu ='''\n
*+       MENU       +* \n
\n
1. Listado con los nombres de archivos del directorio. \n
2. Genere un listado con los nombres de los archivos que comiencen con una letra obtenida al azar (entre todo el alfabeto). \n
3. Genere una lista con aquellos archivos que han sido modificados en los últimos 30 días y que sean de un tamaño menor a una cantidad (en bytes) ingresada por teclado. \n
4. Devuelva el tamaño total de los archivos de imagen (.png, .jpg, .bmp, .jpeg). \n
5. Devuelva  una lista con los nombres de los archivos del directorio ordenados por tamaño. \n
x. Salir. \n
'''
opc = input (menu+'Ingrese opción: ')
seguir = True
while seguir:
	while opc not in ('1','2','3','4','5','x','X'): #si ingresa un no valido, vuelve a preguntar (y a dibujar)
		clear()
		opc = input (menu + 'Opción no válida, intente nuevamente: ')
	print()	
	if opc == 'x' or opc == 'X':
		print('EXIT')
		seguir = False
	else:
		clear()
		ruta = input('Ingrese ruta (enter para actual): ')
		if ruta == '':
			ruta = getcwd()
			#ruta = r"C:\Users\Coya\Downloads" #para probar
		
		if opc == '1' :
			print('Listado con los nombres de archivos del directorio: '+ruta)
			print()
			imprimir(listarchivos(ruta))
			
		elif opc == '2' :
			print('Listado con los nombres de archivos del directorio: '+ruta)
			print()
			generar_lista_azar(ruta)
			
		elif opc == '3' :
			print('Listado con los archivos de menos de 30 dias de antiguadad en ruta: '+ruta)
			print()
			generar_lista_antiguedad_y_tamaño(ruta)
			
		elif opc == '4' :
			print('Tamaño total de los archivos de imagen en: '+ruta)
			print()
			tamaño_total_img(ruta)
			
		elif opc == '5' :
			print('Lista de archivos del directorio {} ordenados por tamaño.'.format(ruta))
			print()
			lista_por_tamaño(ruta)
		
		print()
		print('Presione una tecla para continuar...')
		input()
		clear()
		opc = input (menu+'Ingrese opción: ')

