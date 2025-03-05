import conversion

def shift(text, password, direction):
    textAsInt = conversion.textToNumbers(text)
    passwordAsInt = conversion.textToNumbers(password)

    def shiftPasswordValueToInt(letterIntValue, letterPosition):
        passwordPosition = letterPosition % len(password)
        return (direction(letterIntValue, passwordAsInt[passwordPosition])) % 26

    convertedTextAsInt = []
    
    for index, number in enumerate(textAsInt):
        if isinstance(number, int):
            convertedTextAsInt.append(shiftPasswordValueToInt(number, index))
        else:
            convertedTextAsInt.append(number)

    encryptedText = conversion.numbersToText(convertedTextAsInt)
    encryptedText = conversion.matchUpperCase(encryptedText, text)
    
    return encryptedText

def suma(x, y) : return x+y
def resta(x, y) : return x-y

def encrypt(text, password) :
    return shift(text, password, suma)
def decrypt(text, password):
    return shift(text, password, resta)
