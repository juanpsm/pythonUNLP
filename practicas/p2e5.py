import os
import time

def format_tamaño(T):
	B=' B '
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
	return str(T)+B+' '

def fecha_acc(x):
	t=os.path.getatime(x)
	t=time.localtime(float(t))#convierto a float y luego a tiempo local (no anda sin float)
	return time.strftime("%a, %d %b %Y %H:%M:%S", t) #formateo localtime

def imprimir(lista):
	formato_col='{:<20}|{:>13}|{:>30}'
	print('-'*65)
	print(formato_col.format('Nombre de archivo','tamaño ','fecha último acceso'))
	print('-'*65)
	for x in lista:
		print(formato_col.format(x,format_tamaño(os.path.getsize(x)),fecha_acc(x)))
print('MAYUS:')
Mayus = list(map(lambda x: x.capitalize(),os.listdir('.')))
imprimir(Mayus)
print()
print('ULTIMOS 3 DIAS:')
x3dias = list(filter(lambda x: ((time.time()-os.path.getatime(x))/60/60/24)<3,os.listdir('.')))
imprimir(Mayus)
print()
print('ORDENADA x FECHA:')
Ordenada = list(sorted(os.listdir('.'),key = lambda x: os.path.getatime(x)))
imprimir(Ordenada)
print()
print('SUMA DE TAMAÑOS:')
suma = sum(map(lambda x: os.path.getsize(x),os.listdir('.')))
print(format_tamaño(suma))
