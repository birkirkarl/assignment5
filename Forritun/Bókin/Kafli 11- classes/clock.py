#the class pair

class Pair():
    def __init__(self, v1=0, v2=0):
        self.v1=v1
        self.v2=v2
    def __str__(self):
        return 'Value 1: {},Value 2: {}'.format(self.v1,self.v2)
    def __add__(self,other):
        first=self.v1+other.v1
        second=self.v2+other.v2
        return Pair(first,second)

a= Pair(20,30)
print(a)
b=Pair(40,50)
print(b)
c=a+b
print(c)