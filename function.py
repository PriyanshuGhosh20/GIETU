#functions
def func1():
    print("It's a function")
func1()
def func2(n1,n2):
    print("num1:",n1,"num2:",n2)
func2(10,20)
def func3(n1,n2):
    n3=n1+n2
    return n3
print("Value returned:",func3(100,200))
def func4(n1,n2):
    n3=n1+n2
    return n3
print("Value returned:",func4(100,20.2))

def func5(n1,n2):
    n3=float(n1)+n2
    return n3
print("Value returned:",func5('100',200.22))





