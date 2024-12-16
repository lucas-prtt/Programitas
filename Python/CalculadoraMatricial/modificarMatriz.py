from imprimirMatriz import imprimirMatriz, columnasMatriz, filasMatriz

def modificarMatriz(matriz):
    masCambios = "Si"
    while masCambios == "Si":
        print("Matriz a modificar:")
        imprimirMatriz(matriz)
        while True:
            col = int(input("Indique la Columna: "))-1
            if col < columnasMatriz(matriz) and col >= 0:
                break
        while True:
            fil = int(input("Indique la Fila: "))-1
            if fil < filasMatriz(matriz) and fil >= 0:
                break
        num = float(input("Ingrese el numero a modificar: "))
        matriz[fil][col] = num
        print("Matriz modificada:")
        imprimirMatriz(matriz)
        print("Desea hacer mas cambios?")
        masCambios = input("Ingrese Si o No: ")
        while masCambios != "Si" and masCambios != "No":
            masCambios = input("Ingrse Si o No: ")
    
