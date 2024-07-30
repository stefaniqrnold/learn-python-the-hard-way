from sys import argv 

script, inputFile = argv # saves argv in variables

def printAll(file): # defines funcion with the variable file
    print(file.read()) # read and print file

def rewind(file): # defines funcion with the variable file
    file.seek(0) # sets current file (line) position to a value (0) 

def printALine(lineCount, file): # defines funcion with the variables file and lineCount inside
    print(lineCount, file.readline(), end = "") # prints lineCount and read a line of file (readline automatically changes the line each time it runs)

currentFile = open(inputFile) # open the inputFile (taken from argv) and saves it in currentFile

print("First let's print the whole file:\n")

printAll(currentFile) # prints the whole file

print("Now let's rewind, kind of like a tape.")

rewind(currentFile) # sets current file (line) position to 0

print("Let's print three lines:")

currentLine = 1
printALine(currentLine, currentFile) # call function printALine and sets its parameters to currentLine and currentFile
    # currentFile open the inputFile (taken from argv)

currentLine += 1
printALine(currentLine, currentFile) # repeats above

currentLine += 1
printALine(currentLine, currentFile)
