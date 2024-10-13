from time import sleep


class Queue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__number_of_elements = 0
        self.__queue_elements = []

    def is_empty_queue(self):
        return self.__number_of_elements == 0

    def is_full_queue(self):
        return self.__capacity == 0

    def en_queue(self, element):
        self.__check_if_queue_is_full()
        if not self.is_full_queue(): self.__add_element_to_end_of_queue(element)

    def __check_if_queue_is_full(self):
        if self.is_full_queue(): raise IndexError('Queue is full')


    def __add_element_to_end_of_queue(self, element):
        self.__queue_elements.append(element)
        self.__number_of_elements += 1
        self.__capacity = self.__capacity - 1

        print(self.__queue_elements)

    def front(self):
        return self.__queue_elements[0]

    def back(self):
        return self.__queue_elements[self.__number_of_elements - 1]

    def delete_queue(self):
        self.__remove_element()
        self.__increase_capacity()
        self.__decrease_number_of_elements()

    def __remove_element(self):
        number_of_element: int = self.__number_of_elements
        for index in range(number_of_element):
            index_is_equal_to_the_last_index: bool = index == number_of_element - 1
            if index_is_equal_to_the_last_index:
                self.__queue_elements[index] = None
            else:
                self.__queue_elements[index] = self.__queue_elements[index + 1]
        print(self.__queue_elements)

    def __increase_capacity(self):
        self.__capacity += 1
    def __decrease_number_of_elements(self):
        self.__number_of_elements -= 1