def funcion_rara(uno, dos, *arguments, valor="valor", **keywords):
	print(uno)
	print(dos)
	print(valor)
	print("%%" * 40)
	for arg in arguments:
		print(arg)
	print("%%" * 40)
	for kw in keywords:
		print(kw, ":", keywords[kw])

funcion_rara("uno", "dos", "tres", "cuatro", par1="par1", par3="par3")
