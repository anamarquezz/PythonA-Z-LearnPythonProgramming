class Parent:
    def __init__(self, name):
        print("Parent __init__", name)


class Parent2:
    def __init__(self, name):
        print("Parent2 __init__", name)


class Child(Parent2, Parent):
    def __init__(self):
        print("Child __init__")
        super().__init__("Ana")
        # The super() builtin returns a proxy object hat allows to referer parent class by 'super'
        # Allows us to avoid usign base class expicity
        # Working with Multiple Inheritance
        Parent.__init__(self, "Eric")
        Parent2.__init__(self, "Lidia")


child_obj = Child()
print(Child.__mro__)
