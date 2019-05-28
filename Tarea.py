import os
import string
import random
import datetime


def generar_lista():
	lista=os.listdir()
	return lista


def generar_lista_azar():
	ch=random.choice(string.ascii_letters)
	lista=list(filter(lambda x: x.startswith(ch), os.listdir()))
	return lista, ch

#Genere una lista con aquellos archivos que han sido modificados en los últimos 30 días y que sean de un tamaño menor a una cantidad (en bytes) ingresada por teclado.

 

def lista_restringida(dias=30):
	lista=[]
	s=int(input('Ingrese el límite de tamaño (en bytes) que los archivos no deben superar:'))
	t=datetime.datetime.now().date() - datetime.timedelta(days=dias)
	for a in os.listdir("C:"):
		if os.path.isfile(a):
			if (datetime.datetime.fromtimestamp(os.stat(a).st_mtime).date() > t) and (os.stat(a).st_size < s):
				lista.append(a)
	return lista


#5. Devuelva  una lista con los nombres de los archivos del directorio ordenados por tamaño.

def archivos_por_tamaño():
	l=list(filter(lambda x: os.path.isfile(x), os.listdir()))
	print(sorted(l, key=lambda x: os.stat(x).st_size))
	
	


#print(generar_lista())
print('='*50)
#print(generar_lista_azar())
print('='*50)
print(lista_restringida(5))	
print('='*50)
#archivos_por_tamaño()
