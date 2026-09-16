# -*- encoding: utf-8 -*-
puntaje = {}
puntaje[30] = 'Ada'
puntaje[40] = 'Hedy Lammar'
puntaje[45] = 'Colossus'
puntaje[47] = 'Angela Ruiz Robles'
print(puntaje)
for puntaje,nombre in puntaje.items():
	print('{} puntaje {}'.format(nombre, puntaje))
