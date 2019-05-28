# -*- coding: utf-8 -*-
import traceback
def debug(__x):
	'''Devuelve el nombre_var = valor_var, type: tipo_var'''
	print (traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x,', type:',type(__x))
	
from os import listdir, getcwd, fsencode, scandir, fspath,fsdecode
from os.path import splitext, isfile, join, getsize

def imprimir(lista): #,ruta):

	formato_col='{:<25.30}|{:>15}|{:>15}' #|{:>15.30}'
	print('-'*80)
	print(formato_col.format('Nombre de archivo','isfile?', 'getsize')) #,'fsdecode(x)'))
	print('-'*80)
	for x in lista:
		# ~ print(formato_col.format(x , isfile(x), getsize(x)))
		# ~ print(formato_col.format(x , isfile(join(ruta,x)), getsize(join(ruta,x)),fsdecode(x)))
		print(formato_col.format(x.name , isfile(x), str(x.is_file())))

ruta = input('Ingrese ruta (enter para actual): ')
if ruta == '':
	#ruta = getcwd()
	debug(ruta)
	ruta = r"C:\Users\alumnos"
	'''https://docs.python.org/3/library/os.html
	os.listdir(path='.')
	path may be a path-like object. If path is of type bytes 
	(directly or indirectly through the PathLike interface), 
	the filenames returned will also be of type bytes; 
	in all other circumstances, they will be of type str.
	Note To encode str filenames to bytes, use fsencode().
	See also The scandir() function returns directory entries along with file attribute information, giving better performance for many common use cases.'''
#opcion 1 usar listdir y pasar la ruta como parametro y usar isfile(join(ruta,x)),getsize(join(ruta,x)) 
#opcion 2 usar scandir y .name ó fsdecode(x) para el nombre
#hacer, aparte una funcion que haga la lista de solo archivos con la ruta completa
print("ruta = ",ruta)

#imprimir(listdir(ruta))
#imprimir(listdir(ruta),ruta) #opcion 1 
#imprimir(scandir(ruta))#opcion 2

# ~ for x in(listdir(ruta)):
	# ~ debug(join(ruta,x))

for x in(listdir(ruta)):
	debug(x)
	debug(isfile(x))
	print()

for x in(scandir(ruta)):
	debug(x)
	debug(isfile(x))
	print()
#debug(list(filter(lambda x: isfile(x), listdir("C:"))))
