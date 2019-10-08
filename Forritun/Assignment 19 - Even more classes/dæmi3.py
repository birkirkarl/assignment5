
class Student():
    def __init__(self, student_id,grades):
        self.student_id=student_id
        self.grades=grades

    def __str__(self):
        return 'Student ID: {}\nGrades: {}'.format(self.student_id,self.grades)

    def average(self):
        return sum(self.grades)/len(self.grades)
    def __lt__(self, other):
        if self.average()<other.average():
            return True
        else:
            return False





a = Student(1, [3.0, 4.6, 3.4, 5.4])
b = Student(2, [3.0, 4.6, 3.4, 5.4])

print(a < b)
assert (a < b) == False
print(b)
assert str(b) == "Student ID: 2\nGrades: [3.0, 4.6, 3.4, 5.4]"