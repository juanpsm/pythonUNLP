dic = {1:'uno', 4:'cuatro', 5:'cinco'}

for x in range(1,6):
	try:
		print (dic[x])
	except (KeyError):
		dic[x] = 'nuevo'
print (dic)
		


    
