from imprimirMatriz import imprimirMatriz
opcion = -1
matriz1 = [[1, 2],[3, 4],[5, 6]]
matriz2 = [[1, 2, 3],[4, 5, 6]]

while opcion != 0:
    print("Programa para realizar operaciones con matrices:")
    print("Opciones: ")
    print("0. Salir")
    print("1. Ingresar matriz 1")
    print("2. Ingresar matriz 2")
    print("3. Mostrar matrices")
    print("4. Intercambiar matriz 1 y matriz 2")
    print("5. Calcular el producto entre la matriz 1 y la matriz 2")
    opcion = input("Ingrese una opcion:")
    match(opcion):
        case 0:
            print("Cerrando programa:")
            confirmacion = input("Ingrese Y para confirmar: ")
            if confirmacion != "Y":
                opcion = -1
        case 1:
            matriz1 = ingresarMatriz()
        case 2:
            matriz2 = ingresarMatriz()
        case 3:
            print("Matriz 1: ")
            imprimirMatriz(matriz1)
            print("Matriz 2: ")
            imprimirMatriz(matriz2)
        case 4:
            temp = matriz1
            matriz1 = matriz2
            matriz2 = temp
        case 5:
            resultado = productoMatricial(matriz1, matriz2)
            print("Resultado de la multiplicacion: ")
            imprimirMatriz(resultado)



#if m1 != n2 :
#    input("Error: las columnas de la matriz 2 deben ser iguales a las filas de la matriz 1. ")
#    quit()

