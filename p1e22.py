# -*- encoding: utf-8 -*-
puntaje = {}
puntaje[30] = 'Ada'
puntaje[40] = 'Hedy Lammar'
puntaje[45] = 'Colossus'
puntaje[47] = 'Angela Ruiz Robles'
print('puntaje = ',puntaje)

#for puntaje,nombre in puntaje.items():
#	print('{} puntaje {}'.format(nombre, puntaje))

#print('puntaje.keys() = ',puntaje.keys())

#for puntaje in puntaje.keys():
#	print('puntaje = ',puntaje)

for p in puntaje:
	print('p = ',p)
	
for cada in sorted(puntaje,reverse=True):
	print(puntaje[cada],cada)
