from imprimirMatriz import imprimirMatriz, columnasMatriz, filasMatriz
from ingresarMatriz import ingresarMatriz
opcion = "-1"

while opcion != "0":
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
        case "0":
            print("Cerrando programa:")
            confirmacion = input("Ingrese 0 nuevamente para confirmar: ")
            if confirmacion != "0":
                print("Cancelado")
                opcion = "-1"
        case "1":
            matriz1 = ingresarMatriz()
        case "2":
            matriz2 = ingresarMatriz()
        case "3":
            print("\nMatriz 1: ")
            imprimirMatriz(matriz1)
            print("Matriz 2: ")
            imprimirMatriz(matriz2)
        case "4":
            temp = matriz1
            matriz1 = matriz2
            matriz2 = temp
        case "5":
            if columnasMatriz(matriz1) == filasMatriz(matriz2):
                resultado = productoMatricial(matriz1, matriz2)
                print("Resultado de la multiplicacion: ")
                imprimirMatriz(resultado)
            else: 
                print("Error: las columnas de la matriz 2 deben ser iguales a las filas de la matriz 1. ")
            input()

#if m1 != n2 :
#    input("Error: las columnas de la matriz 2 deben ser iguales a las filas de la matriz 1. ")
#    quit()

