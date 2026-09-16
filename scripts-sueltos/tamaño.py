from os import listdir, getcwd
from os.path import getmtime, isfile, getsize
from time import localtime, strftime, time
from datetime import timedelta

def format_tamaño(T):
	B=' B'
	if T>1024:
		T=round(T/1024,2)
		B=' KB'
		if T>1024:
			T=round(T/1024,2)
			B=' MB'
			if T>1024:
				T=round(T/1024,2)
				B=' GB'
				if T>1024:
					T=round(T/1024,2)
					B=' TB'
	return str(T) + B

def format_fecha_mod(x):
	t=getmtime(x)
	t=localtime(t) #convierto a tiempo local
	#return strftime("%a, %d %b %Y %H:%M:%S", t) #formateo localtime
	return str(timedelta(seconds = time() - getmtime(x)))

def imprimir(lista):
	formato_col='{:<25.20}|{:^15}|{:>30}'
	print('-'*100)
	print(formato_col.format('Nombre de archivo','tamaño','antiguedad modificación'))
	print('-'*100)
	for x in lista:
		print(formato_col.format(x , format_tamaño(getsize(x)), format_fecha_mod(x)))

def antiguedad_en_dias(x):
	#f = (time()- getmtime(x))/60/60/24
	f = timedelta(seconds = time() - getmtime(x))
	return f

#timedelta(days=30)

ruta = input('Ingrese ruta (enter para actual): ')
if ruta == '':
	ruta = getcwd()
print('Listado con los nombres de archivos del directorio: '+ruta)
print()
x3dias = list(filter(lambda x: antiguedad_en_dias(x) < timedelta(days=30) and isfile(x),listdir(ruta)))
ordenada = sorted(x3dias, key=lambda x: getmtime(x))
imprimir(ordenada)
