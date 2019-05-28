def leo_caracteres():
	f = open("lineas.txt","r+")
	for x in f.read():
		print(x)
	f.close()
	

def leo_lineas():
	
	f = open("lineas.txt","r+")
	print(f.readlines())

	f.close()

def otra_forma():
	
	f = open("lineas.txt","r+")
	for linea in f:
		print(linea)
	f.close()

def main():
	
	print('Leo caracteres')
	leo_caracteres()
	print('----------------')
	print('Leo lineas')
	leo_lineas()
	print('----------------')
	print('Otra forma')
	otra_forma()


if __name__ == "__main__":
    main()
