def elemento(x):
	dic = {'art1':'mesa', 'art2':'silla', 'art4':'sillon'}
	try:
		return dic[x]
	except NameError:
		x = 'art1'
