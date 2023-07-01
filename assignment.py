str = input("Enter the string:")

vowels = 'a,e,i,o,u,A,E,I,O,U'
str = str.lower()

for i in str:
    if i in vowels:
        str = str.replace(i,"")

print(str)
