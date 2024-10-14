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
        index = len(self.__itemList) - 1
        while  index >= 0:
            if not self.__itemList[index] is None:
                return self.__itemList[index]
            index = index - 1

    def pop(self):
        index = len(self.__itemList) - 1
        while index >= 0:
            if not self.__itemList[index] is None:
                self.__itemList[index] = None
                index = 0
            index = index - 1
        print(self.__itemList)