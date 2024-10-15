from operator import index


class Map:
    def __init__(self):
        self.__key = []
        self.__value = []
        self.__size: int = 0

    def size(self):
        return self.__size

    def insert(self, key, value):
        if key not in self.__key:
            self.__key.append(key)
            self.__value.append(value)
            self.__size += 1

    def get(self, key):
        for key_index in range(len(self.__key)):
            if self.__key[key_index] == key:
                return self.__value[key_index]

    def contains(self, key):
        if key in self.__key:
            return True

    def update(self, key, value):
        for key_index in range(len(self.__key)):
            if self.__key[key_index] == key:
                self.__value[key_index] = value

    def delete(self, key):
       self.__iterate_through_key_and_delete_key(key)
       print(self.__key)
       # self.__iterate_through_value_and_delete_value(key)
       self.__decrement_size()

    def __iterate_through_key_and_delete_key(self, key):
        last_index_of_list = len(self.__key) - 1

        for key_index in range(len(self.__key)):
            if key_index == last_index_of_list:
                self.__delete_last_key(key_index)


            elif self.__key[key_index] == key and not key_index == last_index_of_list:
                self.__push_the_next_key_to_position_of_the_deleted_key(key_index)
                self.__push_the_key_after_the_previous_pushed_key_to_position_of_previous_pushed_key(key_index)
                self.__turn_key_in_position_of_current_pushed_key_to_none(key_index)

            else:
                current_key = self.__key[key_index]
                print(current_key)
                self.__insert_next_key(key_index, current_key)


    def __insert_next_key(self, key_index, key):
        self.__key[key_index] = key

    def __decrement_size(self):
        self.__size -= 1

    def __delete_last_key(self, key_index):
        self.__key[key_index] = None

    def __push_the_next_key_to_position_of_the_deleted_key(self, key_index):
        self.__key[key_index] = self.__key[key_index + 1]
        self.__key[key_index + 1] = None
        print(self.__key[key_index])
        print(self.__key)
    def __push_the_key_after_the_previous_pushed_key_to_position_of_previous_pushed_key(self, key_index):
        if self.__key[key_index] is not None:
            self.__key[key_index + 1] = self.__key[key_index + 2]
        print(self.__key[key_index + 1])
    def __turn_key_in_position_of_current_pushed_key_to_none(self, key_index):
        self.__key[key_index + 2] = None

    # def __iterate_through_value_and_delete_value(self, key):
    #     last_index_of_value_list = len(self.__value) - 1
    #     index_of_key = self.__get_index_of_key(key)
    #     print(index_of_key)
    #     for value_index in range(len(self.__value)):
    #         if value_index == last_index_of_value_list:
    #             self.__delete_last_value(value_index)
    #             print(self.__value)
    #
    #         elif value_index == index_of_key and not value_index == last_index_of_value_list:
    #             self.__push_the_next_value_to_position_of_the_deleted_value(value_index)
    #             self.__push_the_value_after_the_previous_pushed_value_to_position_of_previous_pushed_value(value_index)
    #             self.__turn_value_in_position_of_current_pushed_value_to_none(value_index)
    #
    #         else:
    #             value = self.__value[value_index]
    #             self.__insert_next_value(value_index, value)
    #
    # def __delete_last_value(self, value_index):
    #     self.__value[value_index] = None
    #
    # def __insert_next_value(self, key_index, value):
    #     self.__value[key_index] = value
    #
    # def __push_the_next_value_to_position_of_the_deleted_value(self, value_index):
    #     self.__value[value_index] = self.__value[value_index + 1]
    #
    # def __push_the_value_after_the_previous_pushed_value_to_position_of_previous_pushed_value(self, value_index):
    #     self.__value[value_index + 1] = self.__value[value_index + 2]
    #
    # def __turn_value_in_position_of_current_pushed_value_to_none(self, value_index):
    #     self.__value[value_index+ 2] = None
    #
    def __get_index_of_key(self, key):
        for key_index in range(len(self.__key)):
            if self.__key[key_index] == key:
                return key_index
