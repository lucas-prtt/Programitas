
globalJsonString = ""

class nuevoObjeto:
    def __init__(self, atributos):   # Atributos es uno o mas duplas (identificador, valor)
        for attr in atributos:
            self.nuevoAtributo(attr[0], attr[1])
        
    def nuevoAtributo(self, id, val):
        setattr(self, id, val)


def parseJson(jsonString):
    global globalJsonString 
    globalJsonString = jsonString
    return matchObjeto()
    # x = nuevoObjeto([("numeroDeLaSuerte", 7), ("edad", 60), ("nombre", "Manuel Belgrano")])



#################
#### match's ####
#################


def matchObjeto():
    atributos = []
    matchCaracter("{")
    quitarEspacios()

    if proximoCaracter() != "}": 
        atributos.append(matchAtributo())
        quitarEspacios()
        while (proximoCaracter() == ','):
            quitarPrimerCaracter()
            quitarEspacios()
            atributos.append(matchAtributo())
    quitarEspacios()
    matchCaracter("}")
    return nuevoObjeto(atributos)



def matchAtributo():
    id = matchTexto()
    quitarEspacios()
    matchCaracter(":")
    quitarEspacios()
    valor = matchValor()
    return (id, valor)

def matchTexto():
    texto = ""
    matchCaracter('"')
    while proximoCaracter() != '"':
        texto = texto + (proximoCaracter())
        quitarPrimerCaracter()
    matchCaracter('"')
    return texto
    
def matchValor():
    if proximoCaracter() == '"':
        return matchTexto()
    elif proximoCaracter() in "-0123456789.":
        return matchNumero()
    elif proximoCaracter() == "[":
        return matchArray()
    elif proximoCaracter() == "{":
        return matchObjeto()
    elif proximaPalabra("true"):
        quitarCaracteres(4)
        return True
    elif proximaPalabra("false"):
        quitarCaracteres(5)
        return False
    elif proximaPalabra("null"):
        quitarCaracteres(4)
        return None
    else:
        raise Exception("Error en funcion matchValor: tipo de valor no identificado")
    

def matchCaracter(caracter):
    global globalJsonString
    if (globalJsonString[0] != caracter) :
        raise Exception("Se esperaba " + caracter + " pero se recibio " + globalJsonString[0])
    else :
        quitarPrimerCaracter()
        return

def matchNumero():
    global globalJsonString
    isFloat = False
    numberVal = 0
    lastNumberIndex = 0
    while globalJsonString[lastNumberIndex] in "0123456789.-":
        if globalJsonString[lastNumberIndex] == '.':
            isFloat = True
        lastNumberIndex += 1 
    if isFloat:
        numberVal = float(globalJsonString[0:lastNumberIndex])
    else:
        numberVal = int(globalJsonString[0:lastNumberIndex])
    quitarCaracteres(lastNumberIndex)
    return numberVal
    
def matchArray():
    matchCaracter("[")
    array = matchArrayAux()
    matchCaracter("]")
    return array

def matchArrayAux():
    quitarEspacios()
    if proximoCaracter() == "{":
        elemento = matchObjeto()
        quitarEspacios()
        if(matchCaracterOpcional(",")) :
            return [elemento] + matchArrayAux()  # Usar append no funciona ya que devuelve None, no la lista con el elemento agregado
        else:                                   # Se puede usar "," pero dicen en internet que no es recomendable porque es ambiguo o algo asi
            return [elemento]
    elif proximoCaracter() in '"1234567890-.':
        elemento = matchValor()
        quitarEspacios()
        if(matchCaracterOpcional(",")) :
            return [elemento] + matchArrayAux() 
        else:
            return [elemento]
    elif proximoCaracter() == "[":
        elemento = matchArray()
        quitarEspacios()
        if(matchCaracterOpcional(",")) :
            return [elemento] + matchArrayAux()
        else:
            return [elemento]    
    else:
        raise Exception("Error en reconocimiento de array")
    

#############################################################
########### Funciones que editan globalJsonString ###########
#############################################################


def proximoCaracter():
    global globalJsonString
    return globalJsonString[0]
def quitarPrimerCaracter():
    global globalJsonString
    globalJsonString = globalJsonString[1:]

def proximaPalabra(palabra):
    global globalJsonString
    temp = globalJsonString
    for c in palabra:
        if temp[0] != c:
            return False
        temp = temp[1:]
    return True

def quitarCaracteres(cuantos):
    for i in range(cuantos):
        quitarPrimerCaracter()

def quitarEspacios():
    global globalJsonString
    while globalJsonString[0] == " ":
        quitarPrimerCaracter()

def matchCaracterOpcional(caracter):
    global globalJsonString
    if globalJsonString[0] == caracter:
        quitarPrimerCaracter()
        return True
    else:
        return False
