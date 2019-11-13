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


#                                    BaseException
#                                        |
#                                     Exception
#           _____________________________|______________________________________________________
#           |                   |                 |                       |                   |
#           |                   |                 |                       |                   |
#     ArthmeticError          OSError        RuntimeError           LookupError       SyntaxError#
#           |                   |                                         |                   |
#           |                   |                                         |                   |
#     ZeroDivisionError         |                                         |              IdentationError
#                               |                                         |
#                               |                                         |
#                      _________|__________                      _________|__________
#                      |                  |                      |                  |
#                      |                  |                      |                  |
#            FileNotFoundError       PermissionError          IndexError         keyError
