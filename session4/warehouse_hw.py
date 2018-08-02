prices = {
    "Banana": 4,
    "Apple": 2,
    "Orange": 1.5,
    "Pear": 3
}

stock = {
    "Banana": 6,
    "Apple": 0,
    "Orange": 32,
    "Pear": 15
}
total_price = 0
for key, value in prices.items():
    print(key)
    print("Price : ", value)
    print("Stock : ", stock[key])
    print(10 * '-*')
    money = value * stock[key]
    total_price += money

print("The total price when you sold out all those fruit is", total_price)

