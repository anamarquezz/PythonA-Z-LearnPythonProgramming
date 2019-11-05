a = [0, 1, 2, 3, 4, 5]

print("\n BREAK")
print("\n------------------------")
print("\n----- for")

for x in a:
    print(x)

i = 0
while i < 5:
    print(i)
    i += 1

print("\n----- while")

for x in a:
    if x == 2:
        break
    print(x)

print("\n")

i = 0
while i < 5:
    if i == 3:
        break
    print(i)
    i += 1

print("\n CONTINUE")
print("\n------------------------")
print("\n----- for")

for x in a:
    if x == 2:
        continue
    print(x)

print("\n----- while")
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
