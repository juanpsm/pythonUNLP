import collections
import traceback
def debug(__x):
	'''Devuelve el nombre_var = valor_var, type: tipo_var'''
	print (traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x,', type:',type(__x))
	
frase = 'Si trabajás mucho con computadoras, eventualmente encontrarás que te gustaría automatizar alguna tarea. Por ejemplo, podrías desear realizar una búsqueda y reemplazo en un gran número de archivos de texto, o renombrar y reorganizar un montón de archivos con fotos de una manera compleja. Tal vez quieras escribir alguna pequeña base de datos personalizada, o una aplicación especializada con interfaz gráfica, o un juego simple.'
lista = frase.upper().replace(',','').replace('.','').replace('?','').split(' ')

c=collections.Counter(lista) #A Counter is a dict subclass for counting hashable objects

print('Frase: ',frase)
print()
print('Palabras mas comunes:',c.most_common(3))
