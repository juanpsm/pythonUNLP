imagenes=['im1','im2','im3']
d={}
for i in imagenes:
	d[i]=[]
	l=1             #para que empiece en x1
	print(i,':')
	print('----')
	print()
	while l in range(4):  #como no empieza en cero hay que hacerlo hasta 4 porque es n-1 el ultimo de range)
		
		t=(input('x%d: '%l),input('y%d: '%l))
		l+=1
		if t in d[i]:
			print('Error ya se encuentran esas coordenadas, intentelo nuevamente..')
			print()
			l-=1
		else:
			d[i].append(t)
			print(t,' --> %s'%i)
			print()
print(d)
