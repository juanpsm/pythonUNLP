import random

def imprimo_tablero():
	for fila in matriz:
			print('-------------')
			print('|'+fila[0]+'|'+fila[1]+'|'+fila[2]+'|')
			print('------------')

def gano(fic):
	for fila in matriz:
		if fila== [fic,fic,fic]:
			return True
	for columna in range(3):
		if matriz[0][columna]==fic and matriz[1][columna]==fic and matriz[2][columna]==fic:
			return True
	if matriz[0][0]==fic and matriz[1][1]==fic and matriz[2][2]==fic or matriz[0][2]==fic and matriz[1][1]==fic and matriz[2][0]==fic:
		return True
	else:
		return False
	

#Creo matriz de juego
matriz=[['   ','   ','   '],['   ','   ','   '],['   ','   ','   ']]

#Infomo que el jugador es X y la computadora O
print('Comenzamos a jugar al juego TA-TE-TI. Yo seré O vos serás X')

#imprimo tablero
imprimo_tablero()

#creo una lista con valores que puede elegir la compu
valores=[0,1,2,3,4,5,6,7,8]

#comienza el proceso de juego: jugador-computadora

juego=True
jugador=True
while juego:
	if jugador:
		#Juega jugador
		#Leo el casillero del jugador y le resto 1 para obtener el elemento de la matriz y, el
		#elemento del elemento de la matriz (fila, columna)
		jugada=int(input('Ingresa el numero de casillero de 1-9: '))-1
		
		#Pregunto si ese casillero no está ocupado
		if matriz[jugada//3][jugada%3]!='   ':
			print ('Ese lugar ya estaba ocupado, perdiste la jugada')
		else:
			#Quito esa posición de valores 
			valores.remove(jugada)
			
		#Asigno ficha
		ficha=' X '
		print('Jugada Jugador')
		#Cambio a jugador compu
		jugador=False
	else:
		#Juega la computadora
		jugada=random.choice(valores)
		
		valores.remove(jugada)
		#Asigno ficha
		ficha=' O '
		print ('Jugada Compu')
		#Cambio a jugador compu
		jugador=True
	
	#Coloco ficha
	matriz[jugada//3][jugada%3]=ficha	
	
	#imprimo tablero
	imprimo_tablero()
	
	#Pregunto si se ganó
	if gano(ficha):
		if ficha==' X ':
			print ('Jugador ganaste!')
		else:
			print ('Jugador perdiste!')
		juego=False
	
