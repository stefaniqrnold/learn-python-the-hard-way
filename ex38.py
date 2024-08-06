tenThings = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Lets fix that.")

stuff = tenThings.split(' ')
moreStuff = ["Day", "Night", "Song", "Frisbee",
             "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    nextOne = moreStuff.pop()
    print("Adding: ", nextOne)
    stuff.append(nextOne)
    print(f"There are {len(stuff)} itens now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
print(' '.join(stuff)) # what? cool!
print('#'.join(stuff[3:5])) # super stellar!