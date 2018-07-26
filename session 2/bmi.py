height = int(input("How tall are you? "))
weight = int(input("How fat are you? "))

bmi = weight/((height/100)*(height/100))
print(bmi)

if 0<= bmi < 16:
    print("Severely underweight")
elif 16<= bmi < 18.5:
    print("Underweight ")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Overweight")
elif bmi >=30:
    print("Obese")
else:
    print("Do you even exsist?")