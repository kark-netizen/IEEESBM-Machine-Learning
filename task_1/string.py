x=input("input as many strings as you want. Seperate by space:\n>")
x=x.split()
count=0
for string in x:
    if len(string)>=4 and string[0]!=string[len(string)-1]:
        count+=1
print(count)