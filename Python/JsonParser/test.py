from parser import *

fileName = input("File name: ")
file = open(fileName, "r")
fileContent = file.read()
elemento = parseJson(fileContent)

print(vars(elemento))
