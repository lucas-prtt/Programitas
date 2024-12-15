from parser import *

#fileName = input("File name: ")
fileName = "test.py"
file = open(fileName, "r")
fileContent = file.read()

parseJson(fileContent)
