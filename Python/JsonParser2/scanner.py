class Token:
    def __init__(self, type, val):
        setattr(self, "type", type)
        setattr(self, "val", val)
    def __repr__(self):
        return "<Objeto Token: Tipo: {}, Valor: {}>".format(self.type, self.val)

def scanNumber(string):
    index = 0
    while index < len(string) and string[index] in "0123456789.-":
        index += 1
    value = float(string[0:index])
    return value, index

def scanString(string):
    index = 0
    index += 1 # Skip de <"> 
    # No toma caracter de escape
    while (index < len(string) and string[index] != '"'):
        index +=1
    index += 1 # Skip de <"> 
    return string[1:index-1], index

def scan(string):
    token, index = proximoToken(string)
    return token, string[index:]

def nextToken(string):
    return proximoToken(string)[0]

def proximoToken(string):
    token = None
    index = 0
    while string[0] == " ":
        string = string[1:]
        index += 1
    match(string[0]):
        case "{":
            index+=1
            token = Token("{", None)
        case "}":
            index+=1
            token = Token("}", None)
        case ":":
            index+=1
            token = Token(":", None)
        case '"':
            value, long = scanString(string)
            index += long
            token = Token("String", value)
        case '[':
            index+=1
            token = Token("[", None)
        case ']':
            index+=1
            token = Token("]", None)
        case ',':
            index+=1
            token = Token(",", None)
        case _:
            if string[0] in "0123456789.-":
                value, long = scanNumber(string)
                index += long
                token = Token("Number", value)
            else:
                raise Exception("Error de scanner en indice del string: {} \n".format(index))
    return token, index