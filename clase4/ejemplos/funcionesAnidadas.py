def proceso_numeros(lista):
	
    def calculo_promedio(lista):
        sum = 0
        for x in lista:
            sum += x
        return (0 if len(lista) == 0 else sum/len(lista))

    min = 9999999
    max = -9999999
 
    for x in lista:
        if (x > max):
            max = x
        if (x < min):
            min = x 

    return (min, max, calculo_promedio(lista))

lista = [1, 2, -3, 14 ]
print(proceso_numeros(lista))



