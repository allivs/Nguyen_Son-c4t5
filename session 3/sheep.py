sheeps = [14, 26, 73, 36, 85, 17, 93, 64, 8]
le = len(sheeps)
c = 0

print("Hello, my name is Son, these are my sheep sizes")
print(*sheeps, sep=" ")
kill = 0
for i in range(le):
    if kill < sheeps[i]:
        kill = sheeps[i]
        c = i
print("Now my biggest sheep has size:", kill, ". Let's shear it")
sheeps[c] = 8

print("After shearing, here is my flock")
print(*sheeps, sep=", ")
print()
s = 0
for k in range(4):
    s += 1
    for i in range(le):
        sheeps[i] += 50
    print("Month", s, ":")
    print("One month has passed, now here is my flock")
    print(*sheeps, sep=", ")

    for i in range(le):
        if kill < sheeps[i]:
            kill = sheeps[i]
            c = i
    print("Now my biggest sheep has size:", kill, ". Let's shear it")
    sheeps[c] = 8
    print()
    print("After shearing, here is my flock")
    print(*sheeps, sep=", ")
    print()

s = 0
for i in range(le):
    s = s + sheeps[i]
print("My flock has size in total:", s)
print("I would get", s, "* 2$ = ", s*20, "$")
print("Thank you! ")
