from scanner import scan, nextToken



class JsonObject:
    jsonString = None
    #def __repr__(self):
    #    return str(self.__dict__)

    def __init__(self, jsonString):
        self.jsonString = jsonString
        self.parse()
        pass
    def match(self, type):
         
        tok, self.jsonString = scan(self.jsonString)
        if tok.type != type:
            raise Exception("Match error: Expected:<{}>, Actual:<{}>".format(type, tok.type))
    def skip(self):
         
        self.match(nextToken(self.jsonString).type)
    def attList(self):
        self.att()
         
        while(nextToken(self.jsonString).type == ","):
            self.match(",")
            self.att()
    def att(self):
        def next() : return nextToken(self.jsonString)
        id = next().val
        self.match("String")
        self.match(":")
        val = self.element()
        setattr(self, id, val)
    def element(self):
        def next() : return nextToken(self.jsonString)
        def skip() : self.skip()
        def delFirstSpaces(string) : 
            while string[0] == " ":
                string = string[1:]
            return string
        val = None
        if next().type in ["String", "Number"]:
            val = next().val
            skip()
        elif next().type == "{":
            self.jsonString = delFirstSpaces(self.jsonString)
            newJsonObjectString = self.jsonString
            index = 1
            opened = 1
            closed = 0
            while(opened > closed):
                if newJsonObjectString[index] == "{":
                    opened += 1
                elif newJsonObjectString[index] == "}":
                    closed += 1
                index +=1
            self.jsonString = self.jsonString[index:]
            newJsonObjectString = newJsonObjectString[0:index]
            val = JsonObject(newJsonObjectString)
            pass
        elif next().type == "[":
            skip()
            val = self.elementList()
            self.match("]")
            pass
        else:
            raise Exception("Unvalid argument <{}>".format(next().type))
        return val
    def elementList(self):
         

        lista = []
        def newElement() : lista.append(self.element())

        lista.append(self.element())
        while(nextToken(self.jsonString).type == ","):
            self.match(",")
            lista.append(self.element())
        return lista


    def parse(self):
        def next() : return nextToken(self.jsonString)
        def match(char) : self.match(char)

        match("{")
        
        if next().type != "}":
            self.attList()

        match("}")
        if self.jsonString != "":
            raise Exception("Basura al final")
        
        delattr(self, "jsonString")

