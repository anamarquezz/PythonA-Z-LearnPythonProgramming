A = [0, 1, 2, 3, 4, 5]          # list
B = (0, 1, 2, 3, 4, 5)          # tuple
C = {0, 1, 2, 3, 4, 5}          # set
D = "Ana"                       # string
E = {"name": "Ana", "age": 28}  # dictionary

# IN
print(2 in A)
print("A" in D)

for i in A:
    print(f"{i}")
print("\n")

for i in D:
    print(f"{i}")

print("\n")
for i in E.values():
    print(i)

print("\n")
for i in E.keys():
    print(i)

print("\n")
for i, y in E.items():
    print(f"key: {i}, Value: {y}")


print("\n")
for x in range(1, 5):
    print(x)


print("\n")
for x in range(1, 10, 2):
    print(x)

print("\n")
for x in range(1, 10, 2):
    print(x)
else:
    print("Loop Completed")
