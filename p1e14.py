imagenes=['im1','im2','im3']

tam={'im1':[(1,2),(10,11)],'im2':[(0,0),(20,20)],'im3':[(0,0),(30,30)]}
d={}
for i in imagenes:
	d[i]=[]
	l=1             #para que empiece en x1
	print(i,':')
	print('tam : (%d,%d),(%d,%d)'%(tam[i][0][0],tam[i][0][1],tam[i][1][0],tam[i][1][1]))
	print('----')
	print()
	while l in range(4):  #como no empieza en cero hay que hacerlo hasta 4 porque es n-1 el ultimo de range)
		
		t=(int(input('x%d: '%l)),int(input('y%d: '%l)))
		l+=1
		if t in d[i]:
			print('Error ya se encuentran esas coordenadas, intentelo nuevamente..')
			print()
			l-=1
		else:  
			#print('t: %d,%d. x_1: %d, x_2: %d, y_1: %d, y_2: %d'%(t[0],t[1],tam[i][0][0],tam[i][1][0],tam[i][0][1],tam[i][1][1]))
			#      x <   x_1       v     x >   x_2         ^    y <    y_1       v   y  >   y_2
			if ((t[0]<tam[i][0][0] or  t[0]>tam[i][1][0]) or (t[1]<tam[i][0][1] or  t[1]>tam[i][1][1])):
				print('esta fuera!')
				l-=1
			else:
				d[i].append(t)
				print(t,' --> %s'%i)
				print()
		
print(d)
