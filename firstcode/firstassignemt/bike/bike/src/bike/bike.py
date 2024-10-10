class Bike:

    def __init__(self, gear=1):
        self._gear:int = gear
        self.__bike_speed: int = 0
        self.__is_bike_on: bool = False


    def _is_bike_on(self):
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

    def accelerate(self):
        if self.__is_bike_on:
            self.accelerate_bike()
        else:
            raise ValueError("bike is off")

    def decelerate(self):
        if self.__is_bike_on:
           self.decelerate_bike()
        else:
            raise ValueError("bike is off")

    def accelerate_bike(self):
        if self.__bike_speed <= 20:
            self.__bike_speed += 1
        elif self.__bike_speed <= 30:
            self._gear = 2
            self.__bike_speed += 2
        elif self.__bike_speed <= 40:
            self._gear = 3
            self.__bike_speed += 3
        elif self.__bike_speed > 41:
            self._gear = 4
            self.__bike_speed += 4

    def decelerate_bike(self):
        if self.__bike_speed <= 20:
            self.__bike_speed -= 1
        elif self.__bike_speed <= 30:
            self._gear = 2
            self.__bike_speed -= 2
        elif self.__bike_speed <= 40:
            self._gear = 3
            self.__bike_speed -= 3
        elif self.__bike_speed > 41:
            self._gear = 4
            self.__bike_speed -= 4