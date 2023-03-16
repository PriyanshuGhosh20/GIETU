one=int(input())
five=int(input())
amt=int(input())
x=amt%5
y=int(amt/5)
if x<=one:
    print(x)
    print(y)
else:
    print(-1)
