from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
fileAgain = input("> ")

txtAgain = open(fileAgain)

print(txtAgain.read())
