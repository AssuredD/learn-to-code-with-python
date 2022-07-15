class Student():
    def __init__(self, math, history, writing):
        self.math = math
        self.history = history
        self.writing = writing

    @property
    def grades(self):
        return self.math + self.history + self.writing

    def __eq__(self, other_student):
        return self.grades == other_student.grades


bob = Student(math=90, history=90, writing=90)
jeff = Student(math=100, history=90, writing=80)
joe = Student(math=40, history=45, writing=50)

print(bob.grades)
print(jeff.grades)
print(joe.grades)

print(bob == jeff)
print(jeff == bob)
print(bob == joe)
print(joe == jeff)

print(bob != joe)
print(joe != jeff)
