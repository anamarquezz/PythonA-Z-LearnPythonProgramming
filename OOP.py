
# Procedure oriente approach
#                       Function1 (sub task1)
# |-----------------|
# |Main Function    |   Function1 (sub task2)
# |-----------------|
#                       Function1 (sub task3)


# Clases and objects in Python

class Student:
    def __init__(self):
        self.name = "Ana"
        self.age = 20
        self.marks = 95

    def talk(self):
        print("Name -", self.name)
        print("Age -", self.age)
        print("Marks -", self.marks)


s1 = Student()
s1.name = "Lidia"
print(s1.name)
s1.talk()

s2 = Student()
print(s2.name)
