import random
from os import system, name 
from time import sleep 
def clear():
	'''Funcion para limpiar la consola. sacada de (https://www.geeksforgeeks.org/clear-screen-python/) '''

	if name == 'nt':
		_ = system('cls') 
	else: 
		_ = system('clear') 

def esperar():
	sleep(0)

def elegir_palabra(tema):
	'''Funcion elegir la palabra secreta, se le da un intiger de 1 a 3 (que es el tema) y devuelve un string'''
	palabras = {1:['gato', 'perro','pato','elefante','lobo'], 2:['rojo','azul','verde','amarillo'], 3:['milanesa','pure','pizza','salchicha']}
	return palabras[tema][random.randrange(len(palabras[tema]))]
	
def horca(c):
	'''Imprimo el dibujo segun un indice que se corresponderá con la cantidad de letras que erró el jugador'''
	ahorcado0 = ''' ___________.._______  
| .__________))______|  
| | / /      () 
| |/ /       ()  
| | /         () 
| |/         ()  
| |         ()) 
| |        //'\\\ 
| |       ()   () 
| |       ()   () 
| |        \\\_// 
| |         `"` 
| |          
| |       
| |          
| |  
| |       
| |                  
""""""""""|"""""""""|"""|   
|"|"""""""'"""""""""'"|"|   
| |                   | |   
: :                   : :    
. .                   . .'''
	ahorcado1 = ''' ___________.._______  
| .__________))______|  
| | / /      ||  
| |/ /       ||.-''.  
| | /        |/  _  \  
| |/         ||  `/,|  
| |          (\\`_.'   
| |           `--'     
| |        
| |        
| |        
| |          
| | 
| |        
| |          
| |  
| |       
| |                  
""""""""""|"""""""""|"""|   
|"|"""""""'"""""""""'"|"|   
| |                   | |   
: :                   : :    
. .                   . .'''
	ahorcado2 = ''' ___________.._______  
| .__________))______|  
| | / /      ||  
| |/ /       ||.-''.  
| | /        |/  _  \  
| |/         ||  `/,|  
| |          (\\`_.'   
| |         .-`--'.   
| |         \ . . / 
| |          |   | 
| |          | . |  
| |          |   |    
| |           \\'/     
| |           
| |           
| |          
| |         
| |         
""""""""""|"""""""""|"""|   
|"|"""""""'"""""""""'"|"|   
| |                   | |   
: :                   : :    
. .                   . .'''
	ahorcado3 = ''' ___________.._______  
| .__________))______|  
| | / /      ||  
| |/ /       ||.-''.  
| | /        |/  _  \  
| |/         ||  `/,|  
| |          (\\`_.'   
| |         .-`--'.   
| |        /Y . . / 
| |       // |   |  
| |      //  | . |     
| |     ')   |   |     
| |           \\'/    
| |           
| |           
| |          
| |         
| |         
""""""""""|"""""""""|"""|   
|"|"""""""'"""""""""'"|"|   
| |                   | |   
: :                   : :    
. .                   . .'''
	ahorcado4 = ''' ___________.._______  
| .__________))______|  
| | / /      ||  
| |/ /       ||.-''.  
| | /        |/  _  \  
| |/         ||  `/,|  
| |          (\\`_.'   
| |         .-`--'.   
| |        /Y . . Y\  
| |       // |   | \\\   
| |      //  | . |  \\\   
| |     ')   |   |   (`    
| |           \\'/      
| |           
| |           
| |          
| |         
| |         
""""""""""|"""""""""|"""|   
|"|"""""""'"""""""""'"|"|   
| |                   | |   
: :                   : :    
. .                   . .'''
	ahorcado5 = ''' ___________.._______  
| .__________))______|  
| | / /      ||  
| |/ /       ||.-''.  
| | /        |/  _  \  
| |/         ||  `/,|  
| |          (\\`_.'   
| |         .-`--'.   
| |        /Y . . Y\  
| |       // |   | \\\   
| |      //  | . |  \\\   
| |     ')   |   |   (`    
| |          ||'||      
| |          || ||   
| |          || ||   
| |          || ||   
| |         / | | \   
| |         `-' `-'    
""""""""""|"""""""""|"""|   
|"|"""""""'"""""""""'"|"|   
| |                   | |   
: :                   : :    
. .                   . .'''
	ahorcado6 = ''' ___________.._______  
| .__________))______|  
| | / /      ||  
| |/ /       ||  
| | /        ||.-''.  
| |/         |/  _  \  
| |          ||  `/,|  
| |          (\\`_.'   
| |         .-`--'.   
| |        /Y . . Y\  
| |       // |   | \\\   
| |      //  | . |  \\\   
| |     ')   |   |   (`   
| |          ||'||     
| |          || ||   
| |          || ||   
| |          || ||   
| |         / | | \   
""""""""""|_`-' `-' |"""|   
|"|"""""""\ \       '"|"|   
| |        \ \        | |   
: :         \ \       : :    
. .          `'       . .'''
	graphix=[ahorcado0,ahorcado1,ahorcado2,ahorcado3,ahorcado4,ahorcado5,ahorcado6]
	return graphix[c]

def cadena_separada(lista):
	'''Funcion para convertir una lista de string (o un conjunto de strings ) 
	a una cadena de sus elementos separados por espacios en blanco'''
	lista=list(lista) # me aseguro que sea una lista
	cad = ''
	for L in lista:		#recorro cada string de la lista
		cad += L[0]+' '   #voy concatenando cada char y un espacio
	return cad

def dibujar():
	'''Este procedimiento agrupa la actualizacion de la pantalla'''
	clear()
	print(horca(cantidad_partes_cuerpo))
	print()
	print(tema[1],':     ',cadena_separada(pistas))  #tema es una variable global (perdon!) que es una tupla tipo ('1','Animal')
	#print('ok/mal : ',cantidad_letras_adivinadas,'/',cantidad_partes_cuerpo) #esto era para ir viendo los aciertos antes que terminara los dibujos
	print('Ya dijiste: ',cadena_separada(letras_dichas)) #Aca voy a mostrar los inputs sucesivos del jugador
		
def intro():
	'''Esta funcion la uso como introduccion al juego y eleccion del tema,
	 devuelve una tupla con dos string: e indice del tema, y un nombre para el tema'''
	clear()
	print(horca(0))
	txt='  Elige un tema:\n   1) Animales\n   2) Colores\n   3) Comidas\n '
	res = input(txt)
	while res not in ('1','2','3'): #si ingresa un no valido, vuelve a preguntar (y a dibujar)
		esperar()
		clear()
		print(horca(0))
		res = input(txt+'Opción no válida :')
	d={1:'Animal',2:'Color',3:'Comida'}
	return (res,d[int(res)])

def validar(letra):
	'''Esta funcion se asegura que el input sea un y solo una letra 
	y que ademas la misma no haya sido ya jugada'''
	while not letra.isalpha():  
		esperar()
		clear()
		dibujar()
		letra = input('Ingresa una LETRA: ').lower()
	while len(letra)>1:
		esperar()
		clear()
		dibujar()
		letra = input('Ingresa UNA letra: ').lower()
	while letra in letras_dichas:
		esperar()
		clear()
		dibujar()
		letra = input('Una que no hayas dicho ya: ').lower()
	return letra

def win():
	'''Mensaje de felicitacion a los ganadores, con algunas estadisticas del juego'''
	sleep(2) #samos suspeso (?
	ESPONJA='''
      .--..--..--..--..--..--.
    .' \  (`._   (_)     _   \\
  .'    |  '._)         (_)  |
  \ _.')\      .----..---.   /
  |(_.'  |    /    .-\-.  \  |
  \     0|    |   ( O| O) | o|    Palabra: {}
   |  _  |  .--.____.'._.-.  |
   \ (_) | o         -` .-`  |    Errores: {}
    |    \   |`-._ _ _ _ _\ /    
    \    |   |  `. |_||_|   | Intentos restantes: {}
    | o  |    \_      \     |     -.   .-.
    |.-.  \     `--..-'   O |     `.`-' .'
  _.'  .' |     `-.-'      /-.__   ' .-'
.' `-.` '.|='=.='=.='=.='=|._/_ `-'.'
`-._  `.  |________/\_____|    `-.'
   .'   ).| '=' '='\/ '=' |
   `._.`  '---------------'
           //___\   //___\ 
             ||       ||
             ||_.-.   ||_.-.
            (_.--__) (_.--__)'''
	clear()
	print()
	print('             ¡¡GANASTE!!')
	print(ESPONJA.format(pal,cantidad_partes_cuerpo,6-cantidad_partes_cuerpo)) #son 7 las imagenes pero la 0 no cuenta porque ya se imprime antes de empezar a jugar

def lose():
	'''Mensaje a los perdedores, con la solucion'''
	SQUID=""" 
        .--'''''''''--. 
     .'      .---.      '. 
    /    .-----------.    \  
   /        .-----.        \ 
   |       .-.   .-.       | 
   |      /   \ /   \      | 
    \    | .-. | .-. |    /  
     '-._| | | | | | |_.-' 
         | '-' | '-' | 
          \___/ \___/  
       _.-'  /   \  `-._ 
     .' _.--|     |--._ '. 
     ' _...-|     |-..._ ' 
            |     | 
            '.___.' 
              | | 
             _| |_ 
            /\( )/\  
           ¡PERDEDOR! 
      La palabra era: {} """
	sleep(5)
	clear()
	print()
	print(SQUID.format(pal))

############### COMIENZA ##################

jugar=True
while jugar:
	#Damos las opciones para elegir el tema
	tema = intro() # devuelve tupla ('indice','tema')
	#Y obtenemos la palabra secreta 
	pal = elegir_palabra(int(tema[0]))
	
	#Inicializamos contadores
	letras_dichas=set()
	cantidad_letras_adivinadas = 0
	cantidad_partes_cuerpo = 0
	pistas = [] 
	for y in pal: #pongo tantos guiones como letras tien la palabra
		pistas.append(['_']) #no pongo espacio porque lo voy a hacer con una funcion mas adelante
	
	fin = False
	while not(fin):
		#limpio la pantalla y dibujo 
		clear()
		dibujar()
		#leo letra ingresada por teclado
		letra = input('Ingresa una letra: ').lower()
		#la validamos y la ingresamos al conjunto de letras jugadas
		letra = validar(letra)
		letras_dichas.add(letra)
		
		if letra in pal: #si acertó tengo que revela las letras	
			for pos in range(len(pal)):
				if pal[pos] == letra: #para eso recorro la palabra actualizo el indice correspondiente en el arreglo de pistas
					pistas[pos] = letra				
					cantidad_letras_adivinadas+=1
			
			#averiguo si terminó o debe continuar
			if cantidad_letras_adivinadas == len(pal):
				win() #muestro mensaje de felicitacion
				fin = True #salgo del segundo while
		else:
			#si se equivocó completo el cuerpo
			cantidad_partes_cuerpo += 1
			if cantidad_partes_cuerpo == 6:  #en este caso son 6 las chances que tiene el jugador por la cantidad de "frames" que le hice al dibujo
				lose()
				fin = True

	j=input('        Jugar de nuevo? (s/n): ') #pregunto y verifico si continua
	while j not in {'s','S','n','N'}:
		j=input()
	jugar= j in {'s','S'}
