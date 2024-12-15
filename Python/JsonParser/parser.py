
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

    if proximoCaracter() != "}": 
        atributos.append(matchAtributo())
        while (proximoCaracter() == ','):
            quitarPrimerCaracter()
            atributos.append(matchAtributo())

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
    elif proximoCaracter() in "0123456789.":
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
    



#############################################################
########### Funciones que editan globalJsonString ###########
#############################################################

def matchCaracter(caracter):
    global globalJsonString
    if (globalJsonString[0] != caracter) :
        raise Exception("Se esperaba " + caracter + " pero se recibio " + globalJsonString[0])
    else :
        quitarPrimerCaracter()
        return

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


