wordlist = ("one", "two", "three", "ten", "i love you")

from random import randint, choice
word = choice(wordlist)
res = [""]
sap = [""]
pos = 0
le = len(word)

for i in range(le):
    sap.append(word[i])
sap.pop(0)
while le > 0:
    pos = randint(1, le)
    res.append(sap[pos-1])
    del sap[pos-1]
    le = len(sap)
print(*res)
answer = input("Your answer: ")
if answer == word:
    print("nailed it, congrats!")
else:
    print("try again, sorry~")
