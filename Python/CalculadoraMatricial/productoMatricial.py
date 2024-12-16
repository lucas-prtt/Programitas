from imprimirMatriz import filasMatriz, columnasMatriz

def productoMatricial(matriz1, matriz2):
    resultado = []
    n = filasMatriz(matriz1)
    m = columnasMatriz(matriz2)
    
    for i in range(n):
        resultado.append([])
        for j in range(m):
            resultado[i].append(valorProductoElemento(matriz1, matriz2, i, j))
    return resultado

def valorProductoElemento(matriz1, matriz2, i, j):
    pasos = columnasMatriz(matriz1)
    valor = 0
    for n in range(pasos):
        valor += matriz1[i][n] * matriz2[n][j]
    return valor