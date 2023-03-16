'''
class Employee:
    def __init__self(self):
        self.employee_id = None
    def check_eligibility(self):
        if(self.employee_id>=9000 and self.employee_id<=10000):
            print("Eligible")
        else:
            print("Not Eligible")
emp1=Employee()
emp1.employee_id=10000
emp1.check_eligibility()
emp2=Employee()
emp2.employee_id=4500
emp2.check_eligibility()
'''

'''
class Example:
    def __init__(self,num):
        self.num=num
    def set_num(self,num):
        self.num=num
    def get_num(self):
        return self.num
obj=Example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())
'''

'''
#1
class Customer:
    def __init__(self):
        self.cust_id=100
c1=Customer()
print(c1.cust_id) #100

#2
class Customer:
    def __init__(self,cust_id):
        self.cust_id=100
c1=Customer(200)
print(c1.cust_id) #100

#3
class Customer:
    def __init__(self,cust_id):
        self.cust_id=cust_id
c1=Customer(200)
print(c1.cust_id) #200
'''

'''
class Book:
    def __init__(self):
        self.title=None
my_fav=Book()
my_fav.title="Head First Programming"
your_fav=Book()
your_fav.title="Learn Python The Hard Way"

my_fav.title="Learning Python"

print("My Fav: ",my_fav.title)
print("Your Fav: ",your_fav.title)
'''

'''
class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
s1=Shoe(1000,"Canvas")
print(s1) #address of object
print(s1.price,s1.material,id(s1))
'''

'''
class Shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
    def __str__(self):
        return "Shoe with price: " + str(self.price) + " and material: " + self.material
s1=Shoe(1000,"Canvas")
print(s1) #returns values
'''
'''
class Mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying details: ")
    def purchase(self):
        self.display()
        print("Calculating price: ")
Mobile().purchase()
m1=Mobile()
print(m1)
m2=Mobile()
print(m2)
'''

'''
class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
        self.total_price=None
    def purchase(self):
        if self.brand=="Apple":
            discount=10
        else:
            discount=5
        self.total_price=self.price - self.price*(discount/100)
        print("Total price of", self.brand, "mobile is", self.total_price)
    def amount_returned(self):
        return (self.price-self.total_price)
mob1=Mobile("Apple",20000)
mob2=Mobile("Samsung",10000)
mob1.purchase()
mob2.purchase()
print("Amount returned of Apple:",mob1.amount_returned())
print("Amount returned of Samsung:",mob2.amount_returned())
'''

'''
class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance #"__var" means private
    def update_balance(self,amount):
        if amount<1000 and amount>0:
            self.__wallet_balance+=amount
    def show_balance(self):
        print("The balance is ",self.__wallet_balance)
c1=Customer(100,"PG",21,1000)
c1.update_balance(500)
c1.show_balance()
'''

'''
#Setter/Getter function
class Customer:
    def __init__(self,cust_id,name,age,wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance #"__var" means private
    def set_balance(self,amount):
        if amount<1000 and amount>0:
            self.__wallet_balance+=amount
    def get_wallet_balance(self):
        return self.__wallet_balance
c1=Customer(100,"PG",21,1000)
print(c1.get_wallet_balance())
c1.set_balance(5000)
print(c1.get_wallet_balance())
'''

'''
class Dam:
    def __init__(self,name,length):
        self.name=name
        self.__length=length
    def get_length(self):
        return self.__length
dam1=Dam("ABC dam",3.5)
print("Dam name:",dam1.name)
print("Dam length:",dam1.get_length())
'''

'''
class Table:
    def __init__(self):
        self.no_of_legs=4
        self.__glass_top=None
        self.__wooden_top=None
    def assign_data(self, glass_top, wooden_top):
        self.__glass_top=glass_top
        self.__wooden_top=wooden_top
    def identify_rate(self, glass_top, wooden_top):
        self.assign_data(glass_top, wooden_top)
        if(self.__glass_top==True):
            rate=20000
        elif (self.__wooden_top==True): 
            rate=30000
    def identify_rate(self, glass_top, wooden_top):
        self.assign_data(glass_top, wooden_top)
        if(self.__glass_top==True):
            rate=20000
        elif (self.__wooden_top==True):
            rate=30000
        else:
            rate=0
        return rate
dining_table=Table()
rate=dining_table.identify_rate (False, True) 
print(rate)
'''

'''
class Table:
    def _init_(self):
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None
dining_table=Table()
back_table=Table()
front_table=back_table
back_table=dining_table
print(dining_table, back_table, front_table)
'''
