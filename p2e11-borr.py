# -*- coding: utf-8 -*-
import pprint
pp = pprint.PrettyPrinter(indent=4)
import traceback
def debug(__x):
	'''Devuelve el nombre_var = valor_var, type: tipo_var'''
	print('****** ',traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x,', type:',type(__x))
	print()



EJ = '''amaga Contemplo. contempló Cigüeña. Utilizando el módulo pattern.es defina una función 
denominada verbosInfinitivos que reciba un string, el cual puede contener varias oraciones
y devuelva una lista de los verbos en infinitivo. hago, baila, voy, hacía, hacía '''

from pattern.es import verbs, conjugate, INFINITIVE, parse, parsetree
from pattern.search import search

#def limpiar_str(cadena):
#	for x in [',','.','?','"','(',')',':','\n']:
#		cadena = cadena.replace(x,' ').replace('  ',' ')
#	return cadena
#parece que el parsetree lo hace solo :v
#parsetree(string,
#   tokenize = True,         # Split punctuation marks from words?
#       tags = True,         # Parse part-of-speech tags? (NN, JJ, ...)
#     chunks = True,         # Parse chunks? (NP, VP, PNP, ...)
#  relations = False,        # Parse chunk relations? (-SBJ, -OBJ, ...)
#    lemmata = False,        # Parse lemmata? (ate => eat)
#   encoding = 'utf-8'       # Input string encoding.
#     tagset = None)         # Penn Treebank II (default) or UNIVERSAL.

def verbosInfinitivos(cadena):
	lis = limpiar_str(cadena).split(' ')
	t = parsetree(cadena)
	verbos = search('VB', t) 
	print('Verbos :', verbos)

#ejemplo de https://www.clips.uantwerpen.be/pages/pattern-search
#from pattern.search import search
#from pattern.en import parsetree
 
#t = parsetree('big white rabbit')
#print(t)
#print()
#print (search('JJ', t)) # all adjectives
#print (search('NN', t) )# all nouns
#print (search('NP', t) )# all noun phrases

#parece que no anda con 3.7

s = EJ
#s = limpiar_str(EJ)
#debug(s)
p = parse(s)
#debug(p)
t = parsetree(s)
#debug(t)
verbos = search('VB*', t)
#debug(verbos)
#print verbos[0].string
print
print
print('  Con search: ')
print(v.string,'->',conjugate(v.string, INFINITIVE))
print()
print ('  Con chunks: ')
for sentence in t:
	for chunk in sentence.chunks:
		#print (chunk.type, [(w.string, w.type) for w in chunk.words])
		if chunk.type == 'VP':
			for w in chunk.words:
				print (w.string,'->',conjugate(w.string, INFINITIVE))
		
#print (conjugate('soy', INFINITIVE))
