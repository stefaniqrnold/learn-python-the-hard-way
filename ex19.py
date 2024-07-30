def cheeseAndCrackers(cheeseCount, boxesOfCrackers): # defines the function with its variables
    print(f"You have {cheeseCount} cheeses!") # print the string with the formated variable
    print(f"You have {boxesOfCrackers} boxes of crackers!")
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function nubers directly:")
cheeseAndCrackers(20, 30)

print("OR, we can use variables from our script:")
amountOfCheese = 10 # saves values to variables
amountOfCrackers = 50

cheeseAndCrackers(amountOfCheese, amountOfCrackers) # saves those variables in the function variables 

print("We can even do math inside too:")
cheeseAndCrackers(10 + 20, 5 + 6) #saves the operations in the function variables

print("And we can combine the two, variables and math:")
cheeseAndCrackers(amountOfCheese + 100, amountOfCrackers + 1000) #saves the operation with the numbers and variables in the funcion variables

def printJorge(qtddJorge):
    print(f"we will print {qtddJorge} Jorges\n", int(qtddJorge) *'jorge')

printJorge(input("how many jorges do you want?\n>"))
