
print("\n **** UNARY MINUS ****")
n = 10
print(f"n = 10 = ", {n})
print(f"-n", {-n})
n = -20
print(f"n = -20 = ", {-n})


print("\n **** RELATIONAL ****")
print(" >           Greayer that                - True if left operand is gratger than the right                X >  y  ")
print(" <           Less that                   - True left operand is les than the ight                        X <  y  ")
print(" ==          Equal to                    - True if both operands are equal                               X == y  ")
print(" !=          Not Equal to                - True if operands are nont equal                               X != y  ")
print(" >=          Grater than or equal to     - True if left operand is greater than or equal to the right    X >= y  ")
print(" <=          Less than or equal to       - True if left operand is less than or equal to the right       X <= y  ")


a = 10
b = 15
print(f"\n a = 10   = ", {a})
print(f" b = 15     = ", {b})

print(f" c= a > b   = ", {a > b})
print(f" c= a >= b  = ", {a >= b})
print(f" c= a < b   = ", {a < b})
print(f" c= a >= b  = ", {a <= b})
print(f" a == b     = ", {a == b})
print(f" a != b     = ", {a != b})


print("\n **** LOGICAL  ****")
print(" and         True if both the operands are true                 x and  y  ")
print(" or          True if either of the operands is true             x or   y ")
print(" not         True if operand is false (complements the operand) not    x  ")

x = 100
y = 200
z = 300
print(f" z > x and z > y = ", {z > x and z > y})
print(f" z > x ", {z > x})
print(f" z > y ", {z > y})
print(f" z > y  and y > z ", {z > y and y > z})
print(f" z > y  or y > z ", {z > y or y > z})

print(f" z > x ", {z > x})
print(f" not z > x ", {not z > x})


print("\n Boolean")
a = True
b = False
print(f" a = {a},  b= {b} ")
print(f" a and b ", {a and a})
print(f" a or b ", {a or b})
print(f" not a ", {not a})
