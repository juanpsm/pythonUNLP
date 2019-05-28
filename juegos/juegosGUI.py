import hangman
import reversegam
import tictactoeModificado
import PySimpleGUI as sg
import json
import time

def main(args):
	sg.ChangeLookAndFeel("SandyBeach")
	usuarios={}
	layout1 = [      
				[sg.Text('Ingrese sus datos: ')],      
				[sg.Text('Username'), sg.InputText("jaja", size=(10,0), key='_NAME_')],      
				[sg.Text('Cantidad de jugadores: '), sg.Text(len(usuarios.keys()), key='_COUNT_')],
				[sg.Button('Aceptar'), sg.Button('Cerrar')]
			]      

	window = sg.Window('Juegos GUI').Layout(layout1)  
	name = ''
	sigo_jugando = True 
	
	event, values = window.Read()  
	if event is None or event == 'Cerrar':  
		sigo_jugando = False
	if event == 'Aceptar':
		name = values['_NAME_']
		usuarios[name]={}
		print('name ',name)
		print('values ',values)
	window.Close()
	
	layout2 = [      
				[sg.Text('Elija el juego, '+name+': ')],      
				[sg.Button('Ahorcado', key='_HANG_')],      
				[sg.Button('TA-TE-TI', key='_TA_')],      
				[sg.Button('Otello', key='_OT_')],      
				[sg.Button('Salir')],
			]  
	window2 = sg.Window('Juegos GUI').Layout(layout2)
	
	
	while sigo_jugando:				# Event Loop  
		event, values2 = window2.Read()
		if event is None or event == 'Salir':
			sigo_jugando = False
			break
		if event == '_HANG_':
			window2.Close()
			hangman.main()
		elif event == '_TA_':
			window2.Close()
			tictactoeModificado.main()
		elif event == '_OT_':
			window2.Close()
			reversegam.main()
		window2 = sg.Window('Juegos GUI').Layout(layout2)
	window2.Close()
	
	print('values ',values)
	print('values2 ',values2)
	

		
if __name__ == '__main__': # If your module is the main program
    import sys
    sys.exit(main(sys.argv))
