a = (10, 15, 20, 25, 30, 10)

print(a[0])

print(a[3])
print(f"a:{a}")
print(f"a.count(): {a.count(10)}")

b = (10, 15, 10, "Ana", 5.5, [10, 5])
print(f"b:{b}")
print(f"a.count(): {b.count(10)}")

print(f"b:{b}")
print(f"len(b): {len(b)}")

a = (10, 20)
b = (30, 40)
c = a + b
print(f"a:{a}, b: {b} : a+b = {c}")
a = c
print(f"a = c : {a}")


p = ("Hello",) * 5
print(f" (Hello,) * 5 = {p}")


print("\n **** Opeations for a tuple ****")
print(" all()            Return True if all elements of the tuple are true ( or if the tuple is empty)")
print(" any()            Return True if any element of the tuple is True, if the tuple is empty return False")
print(" enumerate()      Retun an enumerate object. It contains the indez and value of all the items of tuple as pairs.")
print(" len()            Return the length ( th number of items) in the tuple.")
print(" max()            Return the largest item in the tuple")
print(" min()            Return the smallest item in the tuple")
print(" sorted()         Take elements in the tuple and return a new sorted list (does not sort the tuple itself)")
print(" sum()            Return the sum of all items in the tuple")
print(" tuple()          Convert an iterable (list, string, set, dictionary) to a tuple")


print(f" max(p) = {max(a)}")
print(f" min(p) = {min(a)}")
del(a)
# print(f" del(a) = {a}")/
