import sys  
if sys.version_info[0] >= 3:  
    import PySimpleGUI as sg  
else:  
    import PySimpleGUI27 as sg  
import math
import random
import json
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
#tema=rand_tema()
tema = 'Purple'
sg.ChangeLookAndFeel(tema)

vector =[] #aca voy a guardar los datos
datos = []
arch = ''

#https://github.com/PySimpleGUI/PySimpleGUI/issues/850
layout = [
			[sg.Text('Temperatura'), sg.Slider(range=(-30, 80), orientation='h', size=(35, 20), default_value=0, key='_TEMP_')],
			[sg.Text('Humedad'), sg.Slider(range=(1000, 1200), orientation='h', size=(35, 20), default_value=1020, key='_HUM_')],
			[sg.Button('Añadir', key='_ADD_', pad=((120,5),10))],
			[sg.Listbox(values=[], size=(35, 15), key='_LIST_', pad=(70,10))],
			[sg.Input(key='_BROWSE_', enable_events=True, visible=False)],
			[sg.FileBrowse('Guardar como...', target='_BROWSE_', file_types=(("JSON Files", "*.json"),)),
			sg.Button('Guardar', disabled = True, key='_SAVE_'), sg.Button('Cerrar')]
		 ]      

window = sg.Window('TEMP GUI').Layout(layout)
window.Finalize()

while True:                 # Event Loop  
	event, val = window.Read()  
	#print(event, val)
	if event is None or event == 'Cerrar':  
		break
	if event == '_ADD_':
		
		temp = val['_TEMP_']
		hum = val['_HUM_']
		time = 0
		
		print('Temp:', temp,'Humedad:',hum,'Time:',time)
		
		datos.append({'temp':temp,'humedad':hum,'time':time})
		vector.append(str(temp)+' '+str(hum)+' '+str(time))
		
		window.FindElement('_LIST_').Update(values = vector.copy())
		
		# ~ window.Refresh()
		window.FindElement('_SAVE_').Update(disabled = False)
		
	if event == '_BROWSE_':
		arch = val['_BROWSE_']
		print ('Archivo :',arch)
	if event == '_SAVE_':
		if arch == '':
			arch = open('p3e4.json','w')
		else:
			arch = open(arch,'w')
		for d in window.FindElement('_LIST_').GetListValues() :
			#cadena = d['color']+' '+str(d['coord'][0])+' '+str(d['coord'][1])
			print('Guardo:',d)
		
		# Puedo imprimir en pantalla lo que voy a guardar, con dumps
		# que convierte una estructura tipo diccionario a JSON ydevuelve una cadena
		# ensure_ascii = false para que lea caracteres utf-8 y no solo ascii
		print(json.dumps(datos, sort_keys=False, indent=4, ensure_ascii = False))
		# Con dump escribo la info del diccionario en el archivo, pero antes
		# convirtiendola a JSON
		json.dump(datos, arch)
		arch.close()

window.Close()

