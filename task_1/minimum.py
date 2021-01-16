x=input("Input minimum 5 numbers and separate them by space:\n>")
x=x.split()
x=sorted(x)
count=list()
count=[x[0],1]

for ele in x:
    if ele>count[0]:
        count[0]=ele
        count[1]+=1
    if count[1]==3:
        print(count[0])
        break