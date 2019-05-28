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

layout = [
			[sg.Text('f(x)'),sg.Input('x^2',key='_FUNC_', enable_events=True)], 
			[sg.Button('Plot', key='_DIBUJAR_'), sg.Button('Clear'),sg.Button('Cerrar')],
			[sg.Graph(canvas_size=CANVAS, graph_bottom_left=(0,0), graph_top_right=CANVAS, background_color='black', key='graph')]
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
		print(event, values)
		def f(x):
			exec('f ='+values['_FUNC_'])
			return f
		for x in range(0,CANVAS[0]):
			if (f(x)< CANVAS[1]):
				colorpunto = 'red'
				coordenadas = (x,f(x))
				print('Color:', colorpunto,'Coordenadas:',coordenadas)
				graph.DrawPoint(coordenadas, 2, color=colorpunto)
				window.Refresh()
			else: break
			
	if event == 'Clear':
		graph.Erase()

window.Close()
