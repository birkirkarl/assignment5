class Vehicle():
    def __init__(self, the_license='',the_year=0):
        self.the_license = the_license
        self.the_year = the_year
        self.weight=0
        self.fee=0
    def get_weight(self):
        return self.weight
    def get_fee(self):
        return self.fee
    def get_license(self):
        return self.the_license
    def get_year(self):
        return self.the_year

    def __str__(self):
        return "Vehicle: {} {} Weight={:.2f} Fee=${:.2f}".format(self.the_license,self.the_year, self.weight, self.fee)

#############################################################################
class Car(Vehicle):
    def __init__(self, the_license, the_year, the_style=''):
        super().__init__(the_license, the_year)
        self.the_style = the_style
    def set_weight(self, weight):
        if weight < 3000:
            fee = 30
        elif 3000 <= weight < 5000:
            fee = 40
        else:
            fee = 50
        self.weight = weight
        self.fee = fee
    def get_the_style(self):
        return self.the_style
    def __str__(self):
        return "Car: {} {} {} Weight={:.2f} Fee=${:.2f}".format(self.the_license,self.the_year, self.the_style,self.weight, self.fee)
#############################################################################

class Truck(Vehicle):
    def __init__(self,the_license, the_year=0, the_wheels=0):
        super().__init__(the_license, the_year)
        self.the_wheels = the_wheels
    def set_weight(self, weight):
        if weight < 3000:
            fee = 40
        elif 3000 <= weight and weight < 5000:
            fee = 50
        elif 5000 <= weight and weight < 10000:
            fee = 60
        else:
            fee= 70
        self.weight = weight
        self.fee = fee
    def get_wheels(self):
        return self.the_weels
    def __str__(self):
        return "Truck: {} {} {} wheels Weight={:.2f} Fee=${:.2f}".format(self.the_license ,self.the_year ,self.the_wheels , self.weight , self.fee)
#############################################################################
class Motorbike(Vehicle):
    def __init__(self,the_license, the_year):
        super().__init__(the_license, the_year)
        self.cc = 0
    def set_CC(self, cc):
        if cc < 50:
            fee = 10
        elif 50 <= cc and cc < 200:
            fee = 20
        else:
            fee = 35
        self.cc = cc
        self.fee = fee
    def get_CC(self):
        return self.cc
    def __str__(self): # sleppa því að prenta weight
        return "Motorbike: {} {} {} cc Fee=${:.2f}".format(self.the_license ,self.the_year , self.cc, self.fee)


def main():
    # Create some vehicles
    v1 = Vehicle("AB 123", 2010)
    c1 = Car("SF 735", 2007, "Station")
    t1 = Truck("TU 765", 1994, 6)
    b1 = Motorbike("XY 666", 2005)
    c1.set_weight(3500)
    t1.set_weight(9000)
    b1.set_CC(250)
    # Print info
    print(v1)
    print(c1)
    print("The weight of the car is: {:.2f}".format(c1.get_weight()))
    print(t1)
    print("The fee for the truck is: {:.2f}".format(t1.get_fee()))
    print(b1)
    print("The CC of the bike is: {:.2f}".format(b1.get_CC()))
    print()
    mylist= [str(v1), str(c1), str(t1), str(b1)]
    for i in mylist:
        print(i)
    v1 = c1
    print(v1)
    print()

main()

v1 = Vehicle("SF 456", 2008)

assert v1.get_license() == "SF 456"
assert v1.get_year() == 2008
assert v1.get_fee() == 0.0
assert v1.get_weight() == 0.0

c1 = Car("SK 987", 2002, "Station")
assert c1.get_license() == "SK 987"
assert c1.get_year() == 2002
assert c1.get_fee() == 0.0
assert c1.get_weight() == 0.0
c1.set_weight(3001)
assert c1.get_weight() == 3001
assert c1.get_fee() == 40