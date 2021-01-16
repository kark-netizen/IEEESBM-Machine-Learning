list1= ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n'] 
"""for letter in list1:
    if type(letter)==list:
        print('hello')"""
addlist=['h','i','j']
list1[2][1][2].append(addlist)
print(list1)