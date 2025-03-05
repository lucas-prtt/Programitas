import conversion

def encrypt(text, password):
    textAsInt = conversion.textToNumbers(text)
    passwordAsInt = conversion.textToNumbers(password)

    def addPasswordValueToInt(letterIntValue, letterPosition):
        passwordPosition = letterPosition % len(password)
        return (letterIntValue + passwordAsInt[passwordPosition]) % 26

    convertedTextAsInt = []
    
    for index, number in enumerate(textAsInt):
        if isinstance(number, int):
            convertedTextAsInt.append(addPasswordValueToInt(number, index))
        else:
            convertedTextAsInt.append(number)

    encryptedText = conversion.numbersToText(convertedTextAsInt)
    encryptedText = conversion.matchUpperCase(encryptedText, text)
    
    return encryptedText