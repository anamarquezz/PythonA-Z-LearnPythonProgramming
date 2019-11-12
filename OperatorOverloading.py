a = 10
b = 20
print(a + b)

p = "Hello "
q = "World"
print(p + q)

x = [10, 20, 30]
y = [5, 6, 7]
print(x + y)


class Books:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):  # operator overloading
        return self.pages + other.pages


b1 = Books(100)
b2 = Books(150)


print(b1 + b2)  # b1.__add__(b2)
