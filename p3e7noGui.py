'''7. Dado el archivo que detalla la cantidad de mujeres que estudian carreras tecnológicas,
realizar los siguientes ejercicios:
1. Informar la cantidad total de estudiantes mujeres por universidad.
2. Generar una interfaz en PySimpleGUI que muestre las cantidades agrupadas por universidad ordenadas de mayor a menor.
3. Mostrar las cantidades de cada universidad representadas por algún elemento gráficos
de tamaño proporcional a la cantidad mayor.
4. Incorporar la posibildiad de seleccionar el archivo desde la misma interfaz.
5. Agregar la funcionalidad que el botón que permita ordenar esté deshabilitado hasta
que se seleccione el archivo.
Ver Figura 1 en el cual se puede ver un ejemplo de la interfaz solicitada.
Nota: Investigue en el repositorio github del proyecto PysimpleGUI posibles ejemplos para
utilizar gráficos.'''

import csv
import PySimpleGUI as sg

archi = open("Todas_las_carreras.csv", "r", encoding='utf-8')
csvreader = csv.reader(archi)
next(csvreader) #skips header
todas = {}

# ~ for col in csvreader:
	# ~ todas[col[2]] = 0
# ~ archi.close()

# ~ archi = open("Todas_las_carreras.csv", "r", encoding='utf-8')
# ~ csvreader = csv.reader(archi)
# ~ next(csvreader) #skips header
for col in csvreader:
	try:
		todas[col[2]] += (0 if col[19]=='' else int(col[19]))
	except KeyError:
		todas[col[2]] = (0 if col[19]=='' else int(col[19]))
		
ordeno = sorted(todas.items())
for x in ordeno:
	print('Facultad: {} -- Egresadas: {}'.format(x[0], x[1]))


# ~ for x in list(todas).sorted():
	# ~ print (x)

# ~ archi.seek(0)
# ~ next(csvreader) #skips header
# ~ cont = 0
# ~ for col in csvreader:
	# ~ todas[col[2]] = (0 if col[19]=='' else int(col[19]))
	# ~ if (col[2]=="Universidad Nacional de La Plata"):
		# ~ cont = cont + (0 if col[19]=='' else int(col[19]))
		# ~ print('Año: {} Facultad: {} -- Egresadas: {}'.format(col[0], col[3], ("0" if col[19]=='' else col[19])))
	
# ~ print('\nTotal egresadas de la UNLP: {}'.format(cont))

archi.close()



