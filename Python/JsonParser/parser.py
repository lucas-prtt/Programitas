class nuevoObjeto:
    def __init__(self, atributos):   # Atributos es uno o mas duplas (identificador, valor)
        for attr in atributos:
            self.nuevoAtributo(attr[0], attr[1])
        
        def nuevoAtributo(self, id, val):
            setattr(self, id, val)


def parseJson(jsonString):
    tempJsonString = jsonString
    return matchObjeto(tempJsonString)
    # x = nuevoObjeto([("numeroDeLaSuerte", 7), ("edad", 60), ("nombre", "Manuel Belgrano")])



def matchObjeto(string):
    atributos = []
    # match abreCorchete
    # match atributos
    # match cierraCorchete
    return nuevoObjeto(atributos)








