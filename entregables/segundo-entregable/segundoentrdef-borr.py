import random
import string

from os import system, name, listdir, getcwd, scandir, fsdecode
from os.path import isfile, getmtime, getsize, join

from time import localtime, strftime, time
from datetime import timedelta

import sys  
import PySimpleGUI as sg  



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

def listar_archivos_csv_o_json(ruta):	#------------------------------ Punto 1
	'''Este método que recibe un path como parametro y devuelve una lista de todos los nombres de archivo en el directorio'''
	
	lista = list(filter(lambda x: isfile(x), scandir(ruta)))

	def es_csv_o_json(x):
		return x.name.split('.')[-1] in {'csv', 'json'} # separo el nombre de archivo con los puntos, me quedo con el ultimo elemento de esa estructura y veo si esta en la lista de extensiones
	filtro = list(filter(lambda x: es_csv_o_json(x), lista))
	
	ordenada = sorted( filtro, key=lambda x: getsize(x))

	return ordenada

ruta = getcwd()

# la tabla la cargo con una lista de listas que tienen las filas y una lista que usa como cabecera
#(data, header_list)= ([['a','b','c'],['a1','b1','c1']],['Nombre de archivo','tamaño'])

data = []
for x in listar_archivos_csv_o_json(ruta):
	data.append([x.name,format_tamaño(getsize(x))])
header_list = ['Nombre de archivo','Tamaño']



layout = [[sg.Table(values = data,
					headings=header_list,
					max_col_width=25,
					auto_size_columns=True,
					justification='right',
					alternating_row_color='lightblue',
					num_rows=min(len(data), 20),
					key='_TABLE_')]
					]
window2 = sg.Window('asd').Layout(layout)
window2.Read()