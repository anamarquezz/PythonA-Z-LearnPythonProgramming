class Student:
    def __init__(self, n):
        self.name = n
        print("2nd __init__ method.", self.name)

    def display(self):
        print("Hi")


s1 = Student("Ana")
s1.display()
