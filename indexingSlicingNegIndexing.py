x = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
y = [80, 10, 20, 30, 40, 50, 60, 70, 80, 90]
z = "python"


print(f"\n {x}")
print(f" Indexing:\n x[0]     = {x[0]} \n")


print(f" Slicing: \n  {x}")
print(f"\n x[0:3]   = {x[0:3]}")
print(f" x[0:3:1]   = {x[0:3:1]}")
print(f" x[0:3:3]   = {x[0:7:3]}")
print(f" x[4:]      = {x[4:]}")
print(f" x[:5]      = {x[:5]}")
print(f" x[:]       = {x[:]}")
print(f" x[::2]     = {x[::2]}")
print(f" x[::3]     = {x[::3]}")

print(f" \n Negative Indexing: \n  {x}")
print(f" x[::-1]     = {x[::-1]}")
print(f" z[-3::]     = {z[-3::]}")
print(f" z[0]        = {z[0]}")
print(f" z[-6]       = {z[-6]}")
print(f" z[3:1:-1]   = {z[3:1:-1]}")
print(f" z[4:0:-1]   = {z[4:0:-1]}")
print(f" z[4::-1]   = {z[4::-1]}")
print(f" z[4::-1]   = {z[4::-1]}")
