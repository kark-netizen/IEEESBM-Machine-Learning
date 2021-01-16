inputList = [ 20, 67, 385 ,165 , 52, 33, -19 , 0 , -220 , -66]
def checkDiv(checkList):
    for ele in checkList:
        if ele%33==0 or ele%55==0:
            print(ele,' ', end="")
checkDiv(inputList)