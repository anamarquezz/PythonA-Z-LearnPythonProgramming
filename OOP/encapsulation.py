# in object oriented python program, you can restrit access to methods and variables.
# This can prevent the data from beign modified by accident and is known as encapsulation


class Speed:
    def __init__(self):
        self.speed = 10
        # double underscore means is a private variable, only can be accessed inside that Class
        self.__new_speed = 80

    def get_new_speed(self):
        return self.__new_speed

    def set_new_speed(self, new_speed):
        self.__new_speed = new_speed


s = Speed()
print(s.get_new_speed())
s.set_new_speed(100)

print(s.get_new_speed())
