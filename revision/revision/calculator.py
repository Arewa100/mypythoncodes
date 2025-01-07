class Calculator:
    def __init__(self):
        self._first: int = 0
        self._second: int = 0

    @property
    def _first(self):
        return self.__first

    @_first.setter
    def _first(self, first):
        self.__first = first

    @property
    def _second(self):
        return self.__second

    @_second.setter
    def _second(self, second):
        self.__second = second

    def the_result(self):
        return self._first + self._second