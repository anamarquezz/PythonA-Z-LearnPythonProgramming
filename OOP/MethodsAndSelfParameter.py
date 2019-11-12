
# Procedure oriente approach
#                       Function1 (sub task1)
# |-----------------|
# |Main Function    |   Function1 (sub task2)
# |-----------------|
#                       Function1 (sub task3)


# Understanding init() Method and 'self ' Parameter

class Student:
    def __init__(self):
        self.name = "Ana"
        self.age = 20
        self.marks = 95
        print("__init__ is called")

    def talk(self):
        print("Name -", self.name)
        print("Age -", self.age)
        print("Marks -", self.marks)


s1 = Student()
s1.name = "Lidia"
s1.talk()

s2 = Student()

print("\n")
# Memory
s1 = Student()
print(s1.name)
print(id(s1))

s2 = Student()
print(s2.name)
print(id(s2))
