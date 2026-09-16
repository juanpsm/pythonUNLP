'''Dado un párrafo ingresado por teclado, imprima los 3 verbos más usados en él (en infinitivo,
del más común al menos común), junto con la cantidad de apariciones de cada uno utilizando Counter.
Aclaración: No importa el orden de los verbos cuando tienen igual cantidad de repeticiones.
Utilice el módulo pattern.es.'''
Ejemplo='''
Este es un párrafo de prueba. El verbo ser, será el mas utilizado. El otro será
crear, por eso se creó la oración de esta manera. Por último, se creará esta
oración que posee el tercer verbo: poseer. Nada más que decir.'''
#deberia devolver: ser 4 crear 3 poseer 2

from pattern.es import verbs, conjugate, INFINITIVE, parse, parsetree
from pattern.search import search
import collections
import traceback
def debug(__x):
	'''Devuelve el nombre_var = valor_var, type: tipo_var'''
	print (traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x,', type:',type(__x))


s = input('Ingresar texto (Enter para default): ')
if s == '':
	s = Ejemplo
print ('Frase: ',s)

