x=list()
x=input("Input Age and Name:\n>")
x=x.split()
name=str(x[1])
if int(x[0])<=18 and int(x[0])>0:
    name=name.lower()
elif int(x[0])>18 and int(x[0])<=30:
    name=name[0].upper()+name[1:]
else :
    name=name.upper()
print(name)