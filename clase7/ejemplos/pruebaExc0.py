alum_cod_libros_prestados = {33444555:['a33','a45'], 341122555:['b133'], 40999988:['a22','a45','b77']}

dni_alumno = int(input('Ingresa tu dni'))
while dni_alumno !=0:
    cod_libro = input('Ingresa cod_libro a pedir')
    alum_cod_libros_prestados[dni_alumno].append(cod_libro)
    dni_alumno = int(input('Ingresa tu dni'))


    






