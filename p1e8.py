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
n = input('Nombre de usuario (0 para fin):')
while (n != '0' ):
	if n in usuarios:
		print('Usuario "%s":\n lvl: '%n,usuarios[n]['nivel'],'\n punt: ',usuarios[n]['puntaje'],'\n t: ',usuarios[n]['tiempo'])
	else:
		print('No se encuentra  "%s"'%n)
	n = input('Nombre de usuario (0 para fin):')

