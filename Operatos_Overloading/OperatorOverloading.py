a = 10
b = 20
print(a + b)

p = "Hello "
q = "World"
print(p + q)

x = [10, 20, 30]
y = [5, 6, 7]
print(x + y)


print("\n ** ********************* OPERATOR OVERLOAD ** ********************* ")
print(" OPERATOR             EXPRESSION     INTERNALLY")
print(" Addition             p1 + p2        p1.__add__(p2)")
print(" Substraction         p1 - p2        p1.__sub__(p2)")
print(" Multiplication       p1 * p2        p1.__mul__(p2)")
print(" Power                p1 ** p2       p1.__pow__(p2)")
print(" Division             p1 / p2        p1.__truediv__(p2)")
print(" Floor Division       p1 // p2       p1.__floordiv__(p2)")
print(" Remainder (modulo)   p1 % p2        p1.__mod__(p2)")
print(" Bitwise Left Shift   p1 << p2       p1.__lshift__(p2)")
print(" Bitwise Right Shift  p1 >> p2       p1.__rshif__(p2)")
print(" Bitwise AND          p1 & p2        p1.__and_(p2)")
print(" Bitwise OR           p1 | p2        p1.__or__(p2)")
print(" Bitwise XOR          p1 ^ p2        p1.__xor__(p2)")
print(" Bitwise NOT          ~p1            p1.__invert__()")

print("\n----------------- COMPARISION OPERATOR OVERLOAD  -----------------")
print(" Less Than                   p1 <  p2      p1.__lt__(p2)")
print(" Less than or equal to       p1 <= p2      p1.__le__(p2)")
print(" Equal to                    p1 == p2      p1.__eq__(p2)")
print(" Not Equal to                p1 != p2      p1.__ne__(p2)")
print(" Greater than                p1 >  p2      p1.__gt__(p2)")
print(" Greater than or equal to    p1 >= p2      p1.__ge__(p2)")


class Books:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):  # operator overloading
        return self.pages + other.pages

    def __mul__(self, other):
        return self.pages * other.pages

    def __gt__(self, other):
        return self.pages > other.pages


b1 = Books(100)
b2 = Books(150)

print("\n \n")
print(b1 + b2)  # b1.__add__(b2)
print(b1 * b2)
print(b1 < b2)
