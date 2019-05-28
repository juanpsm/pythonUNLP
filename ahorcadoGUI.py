import sys  
if sys.version_info[0] >= 3:  
    import PySimpleGUI as sg  
else:  
    import PySimpleGUI27 as sg  
import collections
import random

import traceback
def debug(__x):
	'''Devuelve el nombre_var = valor_var, type: tipo_var'''
	print (traceback.extract_stack(limit=2)[0][3][6:][:-1],"=",__x,', type:',type(__x))

def rand_tema():
	raw_temas=  '''GreenTan      
LightGreen      
BluePurple      
Purple      
BlueMono      
GreenMono      
BrownBlue      
BrightColors      
NeutralBlue      
Kayak      
SandyBeach      
TealMono'''
	temas = raw_temas.replace(' ','').split('\n')
	return random.choice(temas)

#print = sg.Print #todo lo que imprimo va a una ventana debug

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


#Damos las opciones para elegir el tema
tema = intro() # devuelve tupla ('indice','tema')
#Y obtenemos la palabra secreta 
pal = elegir_palabra(int(tema[0]))
	
#Inicializamos contadores
Letras_dichas=set()
cantidad_letras_adivinadas = 0
cantidad_partes_cuerpo = 0
pistas = [] 
for y in pal: #pongo tantos guiones como letras tien la palabra
	pistas.append(['_']) #no pongo espacio porque lo voy a hacer con una funcion mas adelante

layout = [
		  [sg.Multiline(default_text='', size=(60,10),font=("Courier"), key='_SCREEN_')],
		  [sg.Text('Elige una letra :', size=(15, 1), key='_ASK_'), sg.InputText(r, key='_IN_')], 
		  [sg.Text('Pistas: ', size=(15, 1)), sg.Text('', key='_PISTAS_')],        
		  [sg.Text('Letras dichas: ', size=(15, 1)), sg.Text('', key='_DICHAS_')],      
		  [sg.Button('Adivinar'), sg.Button('Cerrar')]
		 ]      

window = sg.Window('Ahorcado GUI').Layout(layout)  

while True:                 # Event Loop  
	event, values = window.Read()  
	#print(event, values)
	
	if event is None or event == 'Cerrar':  
		break
	if event == 'Adivinar':
		letra = values['_IN_']
		validar(letra)
		window.FindElement('_NAME_').Update(r)
		window.FindElement('_LVL_').Update(default_dicc[r]['nivel'])
		window.FindElement('_PTS_').Update(default_dicc[r]['puntaje'])
		window.FindElement('_TIME_').Update(default_dicc[r]['tiempo'])
		
		window.FindElement('_COUNT_').Update(len(usuarios.keys()))
		window.FindElement('_LISTA_').Update(cadena(ordenar(usuarios,orden,desc)))
		
window.Close()
