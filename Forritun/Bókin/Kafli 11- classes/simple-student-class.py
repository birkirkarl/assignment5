


class Student():
    def __init__(self, first='', last='', id=0):
        self.first_name= first
        self.last_name= last
        self.id_int= id

    def __str__(self):
        return "{} {}, ID:{}".format(self.first_name, self.last_name, self.id_int)

v1=Student('John','Wade',10)
print(v1)