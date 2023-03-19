def func1 (n1, n2, n3, n4):
    print(n1,n2,n3,n4)
func1(10,"twenty",30.33,True)
def func2 (n1, n2, n3, n4):
    print(n1,n2,n3,n4)
func2(n4=40,n3=30,n2=20,n1=10)
def func3 (n,r,b,c="GIET"):
    print(n,r,b,c)
func3("PG",185,"CSE")
def add(*var): #tuple
    sum1=0
    for i in var:
        sum1=sum1+i
    return(sum1)
print(add(10,20))
print(add(10,20,30))
print()


