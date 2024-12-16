from imprimirMatriz import columnasMatriz, filasMatriz

def determinante(matriz):
    det = 0
    if columnasMatriz(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    elif columnasMatriz(matriz) == 1:
        return matriz[0][0]
    else:
        for i in range(columnasMatriz(matriz)):
            if( i % 2 == 0):
                det += matriz[0][i] * determinante(subMatriz(matriz, 0, i))
            else:
                det -= matriz[0][i] * determinante(subMatriz(matriz, 0, i))
        return det

def subMatriz(matriz, Ni, Nj):
    sub = []
    k = -1
    for i in range(filasMatriz(matriz)):
        if i != Ni:
            sub.append([])
            k += 1
            for j in range(columnasMatriz(matriz)):
                if j != Nj:
                    sub[k].append(matriz[i][j])
    return sub



