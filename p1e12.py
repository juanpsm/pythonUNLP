anim={'Gato Montesadfgsfgfsfshhfddsa':27,'Yacare overo':4,'Boa acuática':5}
for x in anim:
	cadena=''
	index=''
	print(x)
	#print(anim[x])
	for i in range(len(x)):
		#print('i: ',i)
		#print('x[i]: ',x[i])
		if i==anim[x]:
			cadena+=x[i]
		else: 
			cadena+='_'
		if i < 10:
			cadena+=' '
		else:
			cadena+='  '
		index+=str(i)+' '
	print(cadena)
	print(index)
	print()
