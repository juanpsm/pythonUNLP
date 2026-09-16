import random

n = 10 # Es el rango de numeros enteros y también la cantidad de chances para adivinar
i = 1  # Contador
print("Generando número aleatorio entre 0 y "+str(n)+"... Listo!")
r = random.randrange(n)
while i <= n:
	w = input("Adivina el número!  >> ")
	if r == int(w):
		print(w+" es correctou!!")
		i = n + 3  #para que salga del while
	else:
		print(w+" es incorrecto. Intentos restantes: "+ str(n-i))
		i +=1
if i != n + 3: #comprueba que no salio del while por correcto
	print("Te has quedado sin intentos, qué mal..")
