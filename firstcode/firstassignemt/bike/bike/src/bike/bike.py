class Bike:

    def __init__(self, gear=1):
        self.__gear:int = gear
        self.__bike_speed: int = 0
        self.__is_bike_on: bool = False


    def is_bike_on(self):
        return self.__is_bike_on

    def turn_on(self):
        self.__is_bike_on = True

    def turn_off(self):
        self.__is_bike_on = False

    def _bike_speed(self):
        return self.__bike_speed

    @property
    def _gear(self):
        if self.__is_bike_on:
            return self.__gear
        else:
            return "bike is off"

    @_gear.setter
    def _gear(self, gear):
        self.__gear = gear

