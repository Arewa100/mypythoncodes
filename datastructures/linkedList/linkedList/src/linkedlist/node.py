class Node:
    def __init__(self, data):
        self.__data = data
        self.__address_of_the_next_node: Node = None

    def get_data(self):
        return self.__data

    def insert_current_node_at_address(self, new_node):
        self.__address_of_the_next_node = new_node

    def get_linked_node(self):
        return self.__address_of_the_next_node