dic = {1:'juan', 4:'pedro', 5:'elena'}

try:
	print ('Entró al bloque try')
	for x in range(1,6):
		if x == 2 or x == 3:
			raise KeyError
		else:
			print (dic[x])
	print ('continúo el proceso..')
except (KeyError):
	dic[x] = 'nuevo'
	
print ('El diccionario despúes del for', dic)
		


    
