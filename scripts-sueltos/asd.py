import time

listaDeKeys = []

for i in range(10):
	for j in range(10):
		listaDeKeys.append(str(j)+'_'+str(i))


print( listaDeKeys)
if event in listaDeKeys:
	if matriz.celdas[j][i]['marcada']:
							matriz.celdas[j][i]['marcada'] = False
							color_celda = color_celda_default
						else:
							matriz.celdas[j][i]['marcada'] = True
							color_celda = color_celda_marcada
						matriz.celdas[j][i]['color'] = color_celda
						window.FindElement(event).Update(button_color = color_celda)