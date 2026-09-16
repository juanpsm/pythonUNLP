lista1 = ['perro', 4, True, (6,7)]
lista2 = [False, 'casa', 9, [3, 4, 'gato']]
lista3 = []

print('lista1:',lista1)
print('lista2:',lista2)
print('lista3:',lista3)
lista1.extend(lista2)

print('lista1 (mod):',lista1)

for elem in lista1:
	if type(elem) is str:
		lista3.append(elem)
print('lista3 (mod):',lista3)
