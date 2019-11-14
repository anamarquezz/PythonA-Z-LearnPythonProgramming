class TeaException(Exception):
    def __init__(self, arg):
        self.msg = arg


class Tea:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_tea(self):
        if self.__temperature > 85:
            raise TeaException("Tea Too Hot")
        elif self.__temperature < 65:
            raise TeaException("Tea Too Coold")
        else:
            print("Tea OK to Drink")


cup = Tea(100)
cup.drink_tea()
