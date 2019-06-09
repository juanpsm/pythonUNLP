'''Segundo trabajo entregable. Seminario Python 2019. UNLP
Consigna:
Implementar un script que (en una ventana) permita abrir un archivo ".json" o ".csv" y muestre su contenido en una tabla (elemento Table de pysimplegui).
Añada un botón que permita convertir el archivo al otro formato, es decir que si el archivo abierto es ".csv", lo deberá convertir a ".json" y viceversa.
Por ejemplo, si se elige un archivo "jugadores.json", deberá generar "jugadores.csv" (respetando el formato).
Capture las posibles excepciones que pueden surgir en caso que el archivo seleccionado no exista o no tenga los permisos necesarios.


Aclaración: el formato CSV en la primera línea siempre deberá contener los nombres de las columnas.

El ejercicio puede ser realizado en grupo pero se debe subir en forma individual.
Se debe subir un sólo archivo  de nombre Apellido_Segundo_Entregable.py
'''
import sys  
if sys.version_info[0] >= 3:  
    import PySimpleGUI as sg  
else:  
    import PySimpleGUI27 as sg  
import random
import json
import csv
import os
import random
import string

from os import system, name, listdir, getcwd, scandir, fsdecode
from os.path import isfile, getmtime, getsize, join

from time import localtime, strftime, time
from datetime import timedelta

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

# ~ def listarchivos(ruta):	#------------------------------ Punto 1
	# ~ '''Este método que recibe un path como parametro y devuelve una lista de todos los nombres de archivo en el directorio'''
	# ~ #lista = list(map(lambda x: join(ruta,x) , listdir(ruta)))
	# ~ lista = list(filter(lambda x: isfile(join(ruta,x)), listdir(ruta)))
	# ~ lista = list(filter(lambda x: isfile(x), scandir(ruta)))
	# ~ return lista
# ~ def lista_por_tamaño (ruta): #----------------------------- Punto 5
	# ~ '''Este método recibe un path e imprime una lista, ordenada por tamaño, de los archivos contenidos en el directorio'''
	# ~ ordenada = sorted( listarchivos(ruta) , key=lambda x: getsize(x))
	# ~ if ordenada != []:
		# ~ imprimir(ordenada)
	# ~ else : print('No existen archivos en esa ruta.')
# ~ def tamaño_total_img(ruta):
	# ~ '''Este método recibe un path imprime una lista de los archivos contenidos en el directorio 
	# ~ que hayan sido modificados en ese rango de dias y que sean de un tamaño menot al tamaño especificado'''
	# ~ def es_csv(x):
		# ~ return x.name.split('.')[-1] =='csv' # separo el nombre de archivo con los puntos, me quedo con el ultimo elemento de esa estructura y veo si esta en la lista de extensiones de imágenes
	# ~ filtro = list(filter(lambda x: es_csv(x) , listarchivos(ruta)))
	# ~ suma = sum(map(lambda x: getsize(x) , filtro)) #mapea los tamaños en toda la lista de archivos( ya filtrada) y los suma.
	# ~ print(format_tamaño(suma))
	
	
sg.SetOptions(element_padding=(0,0)) 
#aca voy a guardar los datos
data = []
header_list = []
tiene_header = None
nombre_prueba='test_entrega'

menu = [
		[sg.Text('Archivo :',visible=False,size=(30,4),key='_INFO_')],
		[sg.Button('CSV', key='_CSV_'),sg.Button('JSON', key='_JSON_')],
		[sg.Button('Cerrar')]
		]

window = sg.Window('Menu').Layout(menu)

while True:                 # Event Loop  
	event, val = window.Read()  
	#print(event, val)
	if event is None or event == 'Cerrar':  
		break
	if event == '_CSV_':
		header_list = ["tamaño"]
		listaarchivos = list(filter(lambda x: isfile(x) and x.name.split('.')[-1] =='csv', scandir(getcwd())))
		datos = sorted( listaarchivos , key=lambda x: format_tamaño(getsize(x)))
		imprimir(listaarchivos)
		data=[]
		for elemento in datos:
			#print('Elem',elemento)
			data.append(elemento)
		window.Hide()
		layout = [[sg.Table(values = data,
							headings=header_list,
							max_col_width=25,
							auto_size_columns=True,
							justification='right',
							alternating_row_color='lightblue',
							num_rows=min(len(data), 20),
							key='_TABLE_')]
							]
		window2 = sg.Window('csv').Layout(layout)
		window2.Read()
		window.UnHide()
	if event == '_JSON_':
		print('json')
window.Close()
