import sys  
if sys.version_info[0] >= 3:  
    import PySimpleGUI as sg  
else:  
    import PySimpleGUI27 as sg  
import math
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
	
import p3e1_crear

#tema=rand_tema()
tema = 'Purple'
sg.ChangeLookAndFeel(tema)

CANVAS = (800,600)
name_coord = "p3e1_Coord.txt"
name_colors = "p3e1_Colors.txt" #https://github.com/PySimpleGUI/PySimpleGUI/issues/850
layout = [
			[sg.Graph(canvas_size=CANVAS, graph_bottom_left=(0,0), graph_top_right=CANVAS, background_color='black', key='graph')],
			[sg.Input(key='_BROWSE_COL_', enable_events=True, visible=False)], 
			[sg.Input(key='_BROWSE_COORD_', enable_events=True, visible=False)],
			[sg.Button('Crear Archivos (random)', key='_CREAR_'), sg.FileBrowse('CARGAR COLORES', target='_BROWSE_COL_', file_types=(("Text Files", "*.txt"),)),
			sg.FileBrowse('CARGAR COORD', target='_BROWSE_COORD_', file_types=(("Text Files", "*.txt"),)),
			sg.Button('DIBUJAR PUNTOS', key='_DIBUJAR_'), sg.Button('Borrar', key='_CLEAR_'),sg.Button('Guardar', disabled = True, key='_SAVE_'), sg.Button('Cerrar')]
		 ]      

window = sg.Window('PLOT GUI').Layout(layout)

window.Finalize()

graph = window.FindElement('graph')

while True:                 # Event Loop  
	event, values = window.Read()  
	#print(event, values)
	if event is None or event == 'Cerrar':  
		break
	if event == '_CREAR_':
		p3e1_crear.main(CANVAS)
	if event == '_DIBUJAR_':
		print()
		arch_col = open(name_colors,'r')
		arch_coord = open(name_coord,'r')
		vector = []
		p = 0
		for colorpunto in iter(lambda: arch_col.readline(), ''):
			colorpunto = colorpunto.strip().strip()
			coordenadas = arch_coord.readline()
			coordenadas = (int(coordenadas.split(',')[0]),int(coordenadas.split(',')[1]))
			print('Color:', colorpunto,'Coordenadas:',coordenadas)
			vector.append({'color':colorpunto,'coord':coordenadas})
			
			graph.DrawPoint(coordenadas, random.uniform(1,math.sqrt(p)), color=colorpunto)
			window.Refresh()
			p +=1
			
		print('\n Puntos: ',p)
		arch_coord.close()
		arch_col.close()
		window.FindElement('_SAVE_').Update(disabled = False)
		
	if event == '_BROWSE_COL_':
		name_colors = values['_BROWSE_COL_']
		print ('Archivo colores:',name_colors)
	if event == '_BROWSE_COORD_':
		name_coord = values['_BROWSE_COORD_']
		print('Archivo coord:',name_coord)
	if event == '_CLEAR_':
		graph.Erase()
	if event == '_SAVE_':
		arch_mixto = open('p3e1_Mixto.txt','w')
		for d in vector:
			cadena = d['color']+' '+str(d['coord'][0])+' '+str(d['coord'][1])
			print('Guardo:',cadena)
			arch_mixto.write(cadena)
		arch_mixto.close()

window.Close()
