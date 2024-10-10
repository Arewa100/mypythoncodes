class AirCondition:
    def __init__(self):
        self.__is_on = False
        self.__temperature = 16

    def _is_on(self):
        return self.__is_on

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    def temperature(self):
        return self.__temperature

    def increase_temperature(self):
        if self.__is_on:
           self.__increase_the_temperature()
        else:
            raise ValueError('Cannot increase temperature')

    def decrease_temperature(self):
        if self.__is_on:
            self.__decrease_the_temperature()
        else:
            raise ValueError('Cannot decrease temperature')

    def __decrease_the_temperature(self):
        if self.__temperature > 16:
            self.__temperature -= 1

    def __increase_the_temperature(self):
        if self.__temperature < 30:
            self.__temperature += 1