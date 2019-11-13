class Tea:
    def __init__(self, temperature):
        self.__temperature = temperature

    def drink_tea(self):
        if self.__temperature > 85:
            raise ValueError("Tea Too Hot")
            #raise Exception("Tea To Hot")
            #print("Hot to drink")
        elif self.__temperature < 65:
            print("Hot to drink.")
        else:
            print("Tea OK to Drink")


cup = Tea(100)
cup.drink_tea()
