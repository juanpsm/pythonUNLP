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
		'puntaje': 99,
		'tiempo': 10001.1,
	},
}
p_max=0
print('Usuario con mayor puntaje: ')
for n in usuarios:
	if usuarios[n]['puntaje'] > p_max:
		p_max = usuarios[n]['puntaje']
		win = n   #guarda el "registro" ganador
print(win,': ',usuarios[win]['puntaje'])
