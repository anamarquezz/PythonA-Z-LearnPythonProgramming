import builtins
# h = help(builtins)
#  print(h)


result = None

x = int(input("Number 1: "))
y = int(input("Number 2: "))

try:
    result = x / y

except TypeError as e:
    print("Error With Our Code", e)
    print(type(e))


print("New Line")
print("Result = ", result)
