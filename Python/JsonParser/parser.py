
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



def matchObjeto():
    atributos = []
    matchCaracter("{")

    # match atributo
    # while (proximoCaracter(","))
    # {
    # match atributo
    # }


    matchCaracter("}")
    return nuevoObjeto(atributos)





def matchCaracter(caracter):
    global globalJsonString
    if (globalJsonString[0] != caracter) :
        raise Exception("Se esperaba " + caracter + " pero se recibio " + globalJsonString[0])
    else :
        globalJsonString = globalJsonString[1:]
        return

def proximoCaracter(caracter):
    global globalJsonString
    if (globalJsonString[0] != caracter) :
        return False
    else:
        return True


