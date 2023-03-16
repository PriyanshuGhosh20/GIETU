string=input()
char=0
num=0
for i in string:
    if i.isalpha():
        char=char+1
    elif i.isdigit():
        num=num+1
    else:
        continue
list1=[char,num]
print(list1)
