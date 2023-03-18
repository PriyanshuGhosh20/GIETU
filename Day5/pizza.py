# valid pizza types
types=["small","medium"]

class Customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name.title()
        self.__quantity=quantity

    def validate_quantity(self):
        if self.__quantity in range(1,6):
            return True
        else:
            return False
    
    def get_customer_name(self):
        return self.__customer_name
    def get_quantity(self):
        return self.__quantity

class Pizzaservice:
    counter=100
    def __init__(self, customer, pizza_type, additional_topping):
        self.__customer=customer
        self.__pizza_type = pizza_type.lower()
        self.__additional_topping=additional_topping
        self.pizza_cost=0
        self.__service_id=None

    def validate_pizza_type(self):
        if self.__pizza_type in types:
            return True
        else:
            return False

    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and Customer.validate_quantity(self.__customer):
            if self.__pizza_type=="small":
                self.pizza_cost=150*Customer.get_quantity(self.__customer)
                if self.__additional_topping:
                    self.pizza_cost+=35*Customer.get_quantity(self.__customer)
            if self.__pizza_type=="medium":
                self.pizza_cost=200*Customer.get_quantity(self.__customer)
                if self.__additional_topping:
                    self.pizza_cost+=50*Customer.get_quantity(self.__customer)
            if not self.__service_id:
                self.__service_id=self.__pizza_type[0]+str(Pizzaservice.counter+1)
                Pizzaservice.counter+=1
        else:
            self.pizza_cost=-1

    def get_service_id(self):
        return self.__service_id
    def get_pizza_type(self):
        return self.__pizza_type
    def get_customer(self):
        return self.__customer
    def get_additional_topping(self):
        return self.__additional_topping

class Doordelivery(Pizzaservice):
    def __init__(self, customer, pizza_type, additional_topping, distance_in_kms):
        self.__delivery_charge=0
        self.__distance_in_kms=distance_in_kms
        Pizzaservice.__init__(self, customer, pizza_type, additional_topping)

    def validate_distance_in_kms(self):
        if self.__distance_in_kms in range(1,11):
            return True
        else:
            return False

    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            Pizzaservice.calculate_pizza_cost(self)
            if self.pizza_cost!=-1:
                distance=1
                while (distance<=self.__distance_in_kms):
                    if distance in range(1,6):
                        self.pizza_cost+=5
                    if distance in range(6,11):
                        self.pizza_cost+=7
                    distance+=1
        else:
            self.pizza_cost=-1

    def get_delivery_charge(self):
        return self.__delivery_charge
    def get_distance_in_kms(self):
        return self.__distance_in_kms

c=Customer("PG", 5)
p1=Pizzaservice(c, "MEDIUM", True)
p1.calculate_pizza_cost()
print(p1.pizza_cost)
print(p1.get_service_id())

d1=Doordelivery(c, "Medium", True, 6)
d1.calculate_pizza_cost()
print(d1.pizza_cost)
print(d1.get_service_id())

