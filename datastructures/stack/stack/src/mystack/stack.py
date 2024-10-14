class Stack:

    def __init__(self, size):
        self.__size: int = size
        self.__itemList: list = []
        self.__number_of_element: int = 0

    def is_empty(self):
        return True if self.__number_of_element == 0 else False

    def is_full(self):
        return  self.__number_of_element == self.__size


    def push(self, item):
        self.__itemList.append(item)
        self.__number_of_element += 1

    def peek(self):
        return self.__itemList[self.__size - 1]

    def pop(self):
        self.__itemList[self.__number_of_element - 1] = None