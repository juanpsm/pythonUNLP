from pattern.es import singularize, pluralize

def convertir (dicc):
	dicc_nuevo={}
	for x in dicc:
		if x == 's':
			dicc_nuevo['p']=[]
			for i in range(len(dicc[x])):
				dicc_nuevo['p'].append(pluralize(dicc[x][i]))
		if x == 'p':
			dicc_nuevo['s']=[]
			for i in range(len(dicc[x])):
				dicc_nuevo['s'].append(singularize(dicc[x][i]))
	return dicc_nuevo

def convertir_corto(cambiar):
	dicc = {'p':list(map(lambda x : pluralize(x),cambiar['s'])),'s':list(map(lambda x : singularize(x),cambiar['p']))}
	return dicc #por que no anda si hago return {...}??????
			
cambiar = {'s':['gato','caballo', 'silla'],'p': ['informaticas','psicologas', 'ingenieras']}

print ('cambiar : ',cambiar,'\n')

print ('convertir : ',convertir(cambiar),'\n')

print ('convertir_corto : ',convertir_corto(cambiar),'\n')
