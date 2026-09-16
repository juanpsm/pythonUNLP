#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

lado = 50
ANCHO = 10*lado
ALTO = ANCHO
layout = [[sg.Graph(canvas_size=(ANCHO, ALTO), graph_bottom_left=(0,0), graph_top_right=(ANCHO, ALTO), background_color='white', 
			key='_graph_',enable_events=True,drag_submits=True)],
           [sg.T('Change circle color to:'), sg.ReadButton('Red'), sg.ReadButton('Blue'), sg.ReadButton('Move')]]

window = sg.Window('Graph test').Layout(layout).Finalize()
window.Finalize()
graph = window.FindElement('_graph_')
circle =graph .DrawCircle((75,75), 25, fill_color='black',line_color='white')
point = graph.DrawPoint((75,75), 10, color='green')
oval = graph.DrawOval((25,300), (100,280), fill_color='purple', line_color='purple' )
matriz_de_rectangulos = [['' for c in range(ANCHO//lado)]
												for f in range(ALTO//lado)
						]
print(type(ANCHO//lado))

for c in range(0,ANCHO,lado):
	for  f  in range(0,ALTO,lado):
		print(c,f,'->',(c+lado,f+lado))
		# ~ matriz_de_rectangulos[f][c] = graph.DrawRectangle((c*lado,f*lado), ((c+1)*lado,(f+1)*lado), line_color='purple' )
		matriz_de_rectangulos[f//lado][c//lado] = graph.DrawRectangle((c,f), (c+lado,f+lado), line_color='purple' )
print(len(matriz_de_rectangulos))
# ~ for i in range(10):
	# ~ graph.DrawOval((0,i*lado), (lado,(i+1)*lado))
(x1,y1)=(2*lado,1*lado)
(x2,y2)=(5*lado,5*lado)

graph.DrawOval((x1,y1), (x2,y2))

# ~ arc = graph.DrawArc((0,0), (400,400), 160, 10, style='arc' ,arc_color='blue')
while True:
	event, values = window.Read()
	print(event,type(event),values)
	if event is None:
		break
	if event is 'Blue':
		graph.TKCanvas.itemconfig(circle, fill = "Blue")
	elif event is 'Red':
		graph.TKCanvas.itemconfig(circle, fill = "Red")
	elif event is 'Move':
		graph.MoveFigure(point, 10,10)
		graph.MoveFigure(circle, 10,10)
		graph.MoveFigure(oval, 10,10)
	if event is '_graph_':
		graph.DrawPoint((values[event][0],values[event][1]), 10, color='green')
