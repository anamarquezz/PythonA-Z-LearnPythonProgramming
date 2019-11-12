def sumf(n1, n2):
    c = n1 + n2
    return c


num = sumf(10, 20)
print(num)


def sum(inp1, inp2):
    if type(inp1) == type(inp2):
        return inp1 + inp2
    else:
        return "Datatypes are different."


x = sum(10, 15)
print(x)

# --------- Arguments --------------- #

# Positional Arguments

# keyword Argument

# Default Arguments

# variable Length Arguments


def shop(item, price):
    print("Item", item)
    print("Price", price)


def shopV2(item, price=60):
    print("Item", item)
    print("Price", price)


shop("\n Suger", 50)
print("\n")
shop(price=50, item="Sugar")
print("\n")
shopV2(item="Sugar")
print("\n")
shopV2(item="Sugar", price=30)

print("\n\n\n")


def std(name, clas, *marks):
    print("Name: ", name)
    print("clas: ", clas)
    print("marks: ", marks)
    print("\n")
    for x in marks:  # print the value
        print(f"x: {x}")


# inside of marks
std("Ana", 10, 60, 10, 25)

# multiple keyworks
# multiple arguments

print("\n\n\n")

# print the key


def std(name, clas, **marks):
    print("Name: ", name)
    print("clas: ", clas)
    print("marks: ", marks)
    for x, y in marks.items():  # print the key
        print(f"x: {x} :    y: {y}")


std("Ana", clas=10, english=60, maths=95, pysics=25)

std("Ana", clas=10, english=60, maths=95, pysics=25)
