
# TYPES OF ERRORS

# ● Compile-Time Error
# ● Run-Time Error
# ● Logical Error


# COMPILE-TIME ERROR:
#  If we do not follow the proper syntax and semantics of any programming language
#       Example:
#           -Missing colon,
#            -Missin Identation
#
#
# x = 1
# if x == 1
#    print("Hello World")


# RUN-TIME ERROR:
#  Is generated when he program is in running state. They are often termed as an exception.
#   These are the most difficult - and lead to program crashes and bugs in code which can be hard to track down
#       Example:
#           - Lack of Memory,
#           - trying to open a file that was not created
#           - division by 0
#
#print("Hello World")
#x = 1
# if x == 1
#    print("Hello World")

# LOGICAL-TIME ERROR:
#  Occurs due to the poor undestanding of the problem.
#   Wrong formula printing, printin wrong format.
#   Caused because of wrong programming designing.
#
#       Example:
#           - If you want to find the module of a certein number (eg. a%4) instead you wrote
#           the program for division(eg: a/4) then this type of error is considered to be
#           the logical error

# def concat(a, b):
#    print(a + b)

#concat("Hello", 50)

# def inc(sal):
#    sal = sal + sal * 20/100
#    return sal
# sal = inc(1000)
# print("\n Incremented Salary: %.2f" % sal)
