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
print('Usuarios con tiempo distinto de cero: ')
for n in usuarios:
	if usuarios[n]['tiempo'] > 0:
		print(n)
