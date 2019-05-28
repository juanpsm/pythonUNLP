usuarios ={
	'marcos':{
		'nivel': 2,
		'puntaje': 11,
		'tiempo': 6546.7,
	},
	'pancho':{
		'nivel': 1,
		'puntaje': 0,
		'tiempo': 0,
	},
	'ayuwoki':{
		'nivel': 666,
		'puntaje': 666,
		'tiempo': 666,
	},
	'AAAA':{
		'nivel': 999,
		'puntaje': 999999999,
		'tiempo': 10001.1,
	},
}
#n = input('Nombre de usuario (0 para fin):')
#while (n != '0' ):
#	l = int(input('Nivel alcanzado :'))
#	p = int(input('Puntaje máximo :'))
#	t = int(input('Tiempo jugado :'))
#	if n in usuarios:
#		if p > usuarios[n]['puntaje']:
#			usuarios[n]['nivel'] = l
#			usuarios[n]['puntaje'] = p
#			usuarios[n]['tiempo'] = t
#			print('Usuario "%s" actualizado'%n)
#		else:
#			print('No califica')
#	n = input('Nombre de usuario (0 para fin):')

print('.items() = ',usuarios.items())
print()
#print('.keys() = ',usuarios.keys())
#print()
#print('.values() = ',usuarios.values())
#print()

puntajes={}
for x in usuarios:
	puntajes[x]=usuarios[x]['puntaje']
print('puntajes = ',puntajes)
print()

Sort = sorted(usuarios.items(), key=lambda punt: punt[1]['puntaje'],reverse=True)
print('Sort : ',Sort)                        #el 1 es porque es el segundo elemto de la tupla de la lista que generó .items
print()
TopSort = Sort[:2]
print('TopSort : ',TopSort)        # hay que truncar la lista porque la de antes solo la ordenó
print()

from heapq import nlargest
top = nlargest(2, usuarios.items(), key=lambda punt: punt[1]['puntaje'])
print('Top : ',top) 
print()
print('%-10s %-10s'%('User','Puntaje'))
print('------------------')
for x in TopSort:
	print('%-10s %-10s'%(x[0],x[1]['puntaje']))
	print()

	
