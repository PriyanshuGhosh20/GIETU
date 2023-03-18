class WeCare:
    def __init__(self, vid, vtype, vcost):
        self.__vid = vid
        self.__vtype = vtype
        self.__vcost = vcost
        self.__pre_amt = None
        self.set_pre_amt()

    def set_pre_amt(self):
        if self.__vtype == "Two Wheeler":
            self.__pre_amt = 0.02 * self.__vcost
        elif self.__vtype == "Four Wheeler":
            self.__pre_amt = 0.06 * self.__vcost

    def get_pre_amt(self):
        return self.__pre_amt

    def __str__(self):
        return f"Vehicle ID: {self.__vid}\nVehicle Type: {self.__vtype}\nVehicle Cost: {self.__vcost}\nPremium Amount: {self.get_pre_amt()}"

v1 = WeCare(69, "Two Wheeler", 6000)
print(v1)
print()
v2 = WeCare(70, "Four Wheeler", 10000)
print(v2)
