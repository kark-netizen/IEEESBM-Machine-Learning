str=input("Input String:\n>")
count=0
for character in str:
    if character>='A' and character<='Z':
        count+=1
print("Upper Case Characters found:",count)