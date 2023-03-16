string=str(input())
if len(string)>3:
    if string[-3:]=="ing":
        print(string+"ly")
    else:
        print(string+"ing")
else:
    print(string)
