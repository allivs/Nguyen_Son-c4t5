shop = ["T-shirt", "Sweater"]
question = input("Welcome to our shop, what do you want (C,R,U,D)? ")

if question == "C":
    new = input("Enter new item: ")
    shop.append(new)
    print(*shop, sep=", ")

elif question == "R":
    print(*shop, sep=", ")

elif question == "U":
    pos = int(input("Update position? "))
    shop.pop(pos - 1)
    new = input("New item: ")
    shop.append(new)
    print(*shop, sep=", ")

elif question == "D":
    pos = int(input("Delete position: "))
    shop.pop(pos - 1)
    print(*shop, sep=", ")
