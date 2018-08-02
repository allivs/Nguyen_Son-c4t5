sentences = input("Enter a sentence")

sentences = sentences.lower()

alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'

letter_count = {}
for letters in sentences:
    if letters in alphabet:
        if letters in letter_count:
            letter_count[letters] = letter_count[letters] + 1
        else:
            letter_count[letters] = 1

keys = letter_count.keys()
for letters in sorted(keys):
    print(letters, letter_count[letters])
