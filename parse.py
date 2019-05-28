import traceback
def debug(__x):
	'''Devuelve el nombre_var = valor_var, type: tipo_var'''
	print (traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x,', type:',type(__x))
	print()

from pattern.es import parse, split

s = 'El gato negro se sienta en la estera. El gato maulla. Yo mato al gato de un zapatazo'
debug(s)
debug(parse(s))
debug(split(parse(s)))
for sentence in split(parse(s)):
	debug(sentence)
