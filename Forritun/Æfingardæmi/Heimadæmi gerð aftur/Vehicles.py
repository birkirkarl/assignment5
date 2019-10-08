

Vehicle: AB 123 2010 Weight=0.00 Fee=$0.00
Car: SF 735 2007 Station Weight=3500.00 Fee=$40.00
The weight of the car is: 3500.00
Truck: TU 765 1994 6 wheels Weight=9000.00 Fee=$60.00
The fee for the truck is: 60.00
Motorbike: XY 666 2005 250 cc Fee=$35.00
The CC of the bike is: 250.00 
class Vehicle:
    def __init__(self, the_license='',the_year=0):
        self.license=the_license
        self.year=the_year
    def get_weight(self):
        return self.weight
    def get_fee(self):
        return self.fee
    def __str__(self):
        return 'Vehicle: {} {} Weight={:.2f} Fee=${:.2f}'.format(self.license, self.the_year,self.weight,self.fee)
    


class Car(Vehicle):
    def __init__(self,style):
        self.style=style

    def set_weight(self):
        if self.weight < 3000:
            fee=30
        elif 3000 <= self.weight < 5000:
            fee=40
        else:
            fee=50
        return self.fee=fee

    def get_fee(self):
        return self.fee

    def __str__(self):
        return 'Car: {} {} {} Weight={:.2f} Fee=${:.2f}'.format(self.license, self.the_year,self.style,self.weight,self.fee)
class Truck(Vehicle):
    def __init__(self,wheels):
        self.wheels=wheels
    
    def set_weight(self):
        if self.weight < 3000:
            self.fee=40
        elif 3000 <= self.weight < 5000:
            self.fee=50
        elif 5000 <= self.weight < 10000:
            self.fee=60
        else:
            self.fee=70
    
    def set_fee(self):
        return self.fee
0
    def __str__(self):
        return 'Truck: {} {} {} wheels Weight={:.2f} Fee=${:.2f}'.format(self.license, self.the_year,self.wheels,self.weight,self.fee)
class Motorbike(Vehicle):
    def __init__(self, cc):
        self.cc=cc

    def set_CC(self):
        if self.cc < 50:
            self.fee=10
        elif 50 <= self.cc < 200:
            self.fee=20
        else:
            self.fee=30
    def get_CC(self):
        return 'The CC of the bike is: {:.2f}'.format(self.cc)

    def __str__(self):
        return 'Motorbike: {} {} {} cc Weight={:.2f} Fee=${:.2f}'.format(self.license, self.the_year,self.cc,self.weight,self.fee)

 # Create some vehicles
   v1 = Vehicle("AB 123", 2010)
   c1 = Car("SF 735", 2007, "Station")
   t1 = Truck("TU 765", 1994, 6)
   b1 = Motorbike("XY 666", 2005)
   c1.set_weight(3500)
   t1.set_weight(9000)
   b1.set_CC(250)