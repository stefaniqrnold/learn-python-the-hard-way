def for_loop_function(limit, increment):
    numbers = []

    for i in range(0, limit, increment):
        print(f"At the top i is {i}")
        numbers.append(i)
        print(f"Numbers now: {numbers}")
        print(f"At the bottom i is {i}")

    print("The numbers: ")
    for num in numbers:
        print(num)

for_loop_function(3, 1)
for_loop_function(5, 2)