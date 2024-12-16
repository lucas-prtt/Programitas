def imprimirMatriz(matriz):
    espacios = anchoNumerosMatriz(matriz) + (columnasMatriz(matriz)-1) * 3 + 2
    print("┍", end="")
    imprimirEspacios(espacios)
    print("┑")

    for i in range(filasMatriz(matriz)):
        imprimirFila(matriz, i)

    print("┕", end="")
    imprimirEspacios(espacios)
    print("┙")

def imprimirEspacios(n):
    for i in range(n):
        print(" ", end = "")

def filasMatriz(matriz):
    return len(matriz)
def columnasMatriz(matriz):
    return len(matriz[0]) # toma que todas las filas son de igual longitud (de elementos)

def longitudElemento(matriz, fila, columna):
    return len(str(matriz[fila][columna]))
def mayorLongitudColumna(matriz, columna):
    longitudes = []
    for i in range(len(matriz)):
        longitudes.append(longitudElemento(matriz, i, columna))
    return max(longitudes)
def espaciosExtra(matriz, fila, columna):
    return(mayorLongitudColumna(matriz, columna) - longitudElemento(matriz, fila, columna))

def anchoNumerosMatriz(matriz):
    longitudesColumnas = []
    for i in range(columnasMatriz(matriz)):
        longitudesColumnas.append(mayorLongitudColumna(matriz, i))
    return sum(longitudesColumnas)
def imprimirFila(matriz, fila):
    print("│ ", end= "")
    for n, i in enumerate(matriz[fila]):
        imprimirEspacios(espaciosExtra(matriz, fila, n))
        print(i, end = "")
        if n != columnasMatriz(matriz)-1:
            print(" ; ", end= "")
    print(" │")