a = input("Name: ")
b = input("Age: ")
b = input("Marks: ")


class Student:

    def __init__(self, n, a, **m):
        self.name = n
        self.age = a
        self.marks = m

    def display(self):
        print("Hi", self.name)
        print("Your age", self.age)
        print("Your marks:", self.marks)


s1 = Student("Ana ", 22, science=95, english=90, maths=95)
s1.display()
print("------------")
s1 = Student("Lidia ", 22, science=85, english=75, maths=92)
s1.display()
