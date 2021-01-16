scores=list()
n=input("enter number of entries\n>")
inputList=input("enter scores\n>").split()
inputList=sorted(inputList,reverse=True)
for i in inputList:
    if i!=inputList[0]:
        print("runner up is",i)
        break