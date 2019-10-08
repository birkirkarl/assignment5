
class MyString():
    def __init__(self, strengur=''):
        self.strengur=strengur
    
    def lengd_strengs(self):
        lengd=len(self.strengur)
        return lengd
    
    def __gt__(self, other):
        if self.lengd_strengs()>other.lengd_strengs():
            return True
        else:
            return False

    def __sub__(self, other):#subtraction
        return self.lengd_strengs()-other.lengd_strengs()


obj1= MyString('sdfsadfadsfasdfasfasdfasdfasdfasdf')
obj2= MyString('alireza')
print(obj1>obj2)
print(obj1 - obj2)