
def letterToNumber(letra):
    ascii = ord(letra)
    if 65 <= ascii <= 90:
        return ascii - 65
    elif 97 <= ascii <= 172:
        return ascii - 97
    else:
        return letra

def numberToLetter(number):
    if isinstance(number, int):
        letter = chr(number + 97)
    else:
        letter = number
    return letter

def textToNumbers(text) : return list(map(letterToNumber, text))
def numbersToText(numbers) : return list(map(numberToLetter, numbers))

def matchUpperCase(text, reference):
    newText = ""
    for i, j in zip(text, reference):
        if j.isupper():
            newText += i.upper()
        else:
            newText += i
    return newText



