import vigenere
while(True):
    operacion = 0
    while(operacion not in (1, 2, 3)):
        operacion = int(input("Select an option: \n 1. Encript\n 2. Decript\n 3. Salir\n >"))

    match(operacion):
        case 1:
            text = input("Input text to encrypt: ")
            password = input("Input password: ")
            print("Encripted text: " + vigenere.encrypt(text, password))
        case 2: 
            text = input("Input text to decrypt: ")
            password = input("Input password: ")
            print("Decripted text: " + vigenere.decrypt(text, password))
            pass
        case 3:
            quit()

