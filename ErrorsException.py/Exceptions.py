# run time error

print("Hello")


def concat(a, b):
    print(a + b)


concat("Hello", 50)

#                              BaseException
#                                    |
#                                 Exception
#                       _________________|_________________
#                       |                                 |
#                   StandardError                       Warning
#                       |                                  |
#     ArthmeticError ---|                                  |--- DeprecationWarning
#     AssertionError ---|                                  |--- RuntimeWarning
#     SyntaxError    ---|                                  |--- ImportWarning
#     TypeError      ---|
#     EOFError       ---|
#     RuntimeError   ---|
#     ImportError    ---|
#     NameError      ---|
