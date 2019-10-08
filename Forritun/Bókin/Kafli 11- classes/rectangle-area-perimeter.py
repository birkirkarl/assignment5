



class Rectangle():
    def __init__(self, length=0, width=0):
        if length<=0:
            self.length=0
        else:
            self.length=length
        if width<=0:
            self.width=0
        else:
            self.width=width
    def area(self):
        svaedi=self.length*self.width
        return svaedi
    def perimeter(self):
        Perimeter=2*(self.length+self.width)
        return Perimeter
    def __str__(self):
        return "Length: {}, Width: {}".format(self.length, self.width)
    def __repr__(self):
        return 'Rectangle({},{})'.format(self.length,self.width)
    def __eq__(self,other):
        if self.area()==other.area():
            return True
        else:
            return False

obj1 = Rectangle(2,3)
print(obj1.area()) == print('6')
print(obj1.perimeter()) == print('10')
print(obj1) == print('Length: 2, Width: 3')

assert obj1.area() == 6
assert obj1.perimeter() == 10
assert str(obj1) == 'Length: 2, Width: 3'