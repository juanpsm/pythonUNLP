# -*- coding: utf-8 -*-
EJ = '''amaga Contemplo. contempló Cigüeña. Utilizando el módulo pattern.es defina una función 
denominada verbosInfinitivos que reciba un string, el cual puede contener varias oraciones
y devuelva una lista de los verbos en infinitivo. hago, baila, voy, hacía, hacía '''

from pattern.es import verbs, conjugate, INFINITIVE, parse, parsetree
from pattern.search import search

def verbosInfinitivos(cadena):
	t = parsetree(cadena)
	verbos = search('VB*', t) 
	#lis=verbos.match.string
	#print 'list: ',lis
	#print #no puedo convertirlo a lista de una??
	lista =[]
	for match in verbos:
		lista.append((match.string , conjugate(match.string, INFINITIVE)))
	#print 'lista for: ',lista
	#print lista[3][1] 
	return lista

s = raw_input('Ingresar texto (Enter para default): ')
if s == '':
	s = EJ
print 'Frase: ',s
result = verbosInfinitivos(s)
print 'Verbos :'
for x in result:
	print '\t',x[1]
#revisar borrador. 
# Error de unicode, cuando hace parse o search y cuando imprime la consola
# forma sin recorrer search??
#
