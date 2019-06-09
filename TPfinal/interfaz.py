import PySimpleGUI as sg
import random
import string

color_celda_marcada = ('#EFF0D1','#D33F49') #blanco y rojo
color_celda_default = ('#262730','#77BA99') #negro y verde


ANCHO = 7
ALTO = 8

sg.SetOptions(
background_color='#EFF0D1',
text_element_background_color='#EFF0D1', 
element_background_color='#EFF0D1',
scrollbar_color=None,
input_elements_background_color='#D7C0D0', #lila
progress_meter_color = ('green', 'blue'),
button_color=color_celda_default
)
FUENTES=['Arial','Courier','Comic','Fixedsys','Times','Verdana','Helvetica']
fuente = FUENTES[3]
fila=[str(i) for i in range(ANCHO)]
#print(fila)
matriz=[
		[{'key':str(j)+'_'+str(i),'marcada':False,'letra':random.choice(string.ascii_uppercase)} for i in range(ANCHO)]
		for j in range(ALTO)
]
matriz.append('end')
print(matriz)
layout = [
			[sg.Button(matriz[j][i]['letra'],
			 size=(4,2), 
			 pad=(5,5), 
			 font=fuente,
			 key = str(j)+'_'+str(i)) for i in range(ANCHO)]
		for j in range(ALTO)
		 ]
layout.append([sg.Button('Cerrar')])
window = sg.Window('TEMP GUI').Layout(layout)
window.Finalize()

while True:                 # Event Loop  
	event, val = window.Read()  
	#print(event, val)
	if event is None or event == 'Cerrar':  
		break
	# ~ if any([event in matriz[j] for j in range(ALTO)]):
	for i in range(ANCHO):
		for j in range(ALTO):
			if (matriz[j][i]['key'] == event ):
				if matriz[j][i]['marcada']:
					matriz[j][i]['marcada'] = False
					color_celda=color_celda_default
				else:
					matriz[j][i]['marcada'] = True
					color_celda = color_celda_marcada
				#print(matriz)
				window.FindElement(event).Update(button_color = color_celda)
	window.Refresh()

window.Close()
