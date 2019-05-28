#user = {
#  'nivel': '2',
#  'puntaje': '6',
#  'tiempo': '6',
#}
#usuarios ={'marcos':user}
#print (usuarios['marcos']['nivel'])
usuarios ={}
n = input('Nombre de usuario (0 para fin):')
while (n != '0' ):
	while n in usuarios:
		n = input('Ese nombre se encuentraen uso, elija otro: ')
	usuarios[n] = {}
	usuarios[n]['nivel'] = input('Nivel alcanzado :')
	usuarios[n]['puntaje'] = input('Puntaje máximo :')
	usuarios[n]['tiempo'] = input('Tiempo jugado :')
	print('Usuario "%s" agregado'%n)
	n = input('Nombre de usuario (0 para fin):')

print(usuarios)
