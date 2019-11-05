x = ["ana", 22, "CSE", "Python", 55.5]
print(x[2])

y = x[3]
print(y)
print(f" length: {len(x)}")
x.insert(0, "Eric")
print(f"\n {x}")

nums = [22, 55, 80, 7, 15]
print(f"\n nums: {nums}")
nums.sort()
print(f"Sort :::::: {nums}")


print(f"\n\n x: {x}")
x.remove("CSE")
print(f"Remove [CSE] ---->  {x}")
print(f"\n x: {x}")
x.reverse()
print(f"Reverse ---->  {x}")
print(f"\n x: {x}")
x.pop()
print(f"Remove last element ----> {x}")


x = ["ana", 22, "CSE", "Python", 55.5]
print(f"\n x: {x}")
x.clear()
print(f"clear last element ----> {x}")


x = ["ana", 22, "CSE", "Python", 55.5]
print(f"\n x: {x}")
print(f"count(22) element ----> {x.count(22)}")


x = ["ana", 22, "CSE", "Python", 55.5]
print(f"\n x: {x}")
x.append("lala")
print(f"append element ----> {x}")


x = ["ana", 22, "CSE", "Python", 55.5]
print(f"\n x: {x}")
del x
print(f"delete last element ----> {x}")
