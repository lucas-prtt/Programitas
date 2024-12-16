from imprimirMatriz import imprimirMatriz, columnasMatriz, filasMatriz
def ingresarMatriz():
    print("\n")
    n = int(input("Ingrese la cantidad de filas: "))
    m = int(input("Ingrese la cantidad de columnas: "))
    tempMatriz = []
    for i in range(n):
        tempMatriz.append([])
        for j in range(m):
            tempMatriz[i].append(" X ")
    
    for i in range(n):
        for j in range(m):
            remplazarPrimeraX(tempMatriz)
            imprimirMatriz(tempMatriz)
            numero = input("Ingrese el numero en la posicion ({}, {}) : ".format(str(i+1), str(j+1)))
            if numero == "":
                numero = "0"
            tempMatriz[i][j] = float(numero)
        
    print("\n\nMatriz final: ")
    imprimirMatriz(tempMatriz)
    return tempMatriz

def remplazarPrimeraX(matriz):
    i = 0
    j = 0
    while i < filasMatriz(matriz) and matriz[i][j] != " X " :
        j+=1
        if j >= columnasMatriz(matriz):
            j = 0
            i += 1
    matriz[i][j] = "▯"


