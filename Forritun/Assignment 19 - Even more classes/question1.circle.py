from math import pi

class Circle:
    def __init__(self, radius):
        self.set_radius(radius)
    
    def area(self):
        return self.__radius ** 2 * pi
    
    def perimeter(self):
        return 2*pi*self.__radius
    
    def set_radius(self,radius):
        self.__radius = float(radius)
        
    def get_radius(self):
        return self.__radius
    
    def __str__(self):
        return 'Area: {:.2f}\nPerimeter: {:.2f}'.format(self.area(),self.perimeter())