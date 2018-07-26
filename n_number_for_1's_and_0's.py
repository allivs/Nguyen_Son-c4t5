n = int(input("Enter a number: "))

for i in range(0, n):
    if i % 2 == 0:
        print("0", end=" ")
    else:
        print("1", end=" ")