from src.linkedlist.node import Node

class LinkedList:
    def __init__(self):
        self.__head: Node = None
        self.__last: Node = None
        self.__size: int = 0

    def is_empty(self):
        return self.__head_is_empty()

    def __head_is_empty(self):
        return self.__head is None

    def insert(self, data):
        if not self.is_empty(): self.__insert_when_list_is_not_empty(data)
        if self.is_empty(): self.__insert_when_list_is_empty(data)

    def __insert_when_list_is_empty(self, data):
        new_node: Node = Node(data)
        self.__head = new_node
        self.__last = new_node

    def __insert_when_list_is_not_empty(self, data):
        new_node: Node = Node(data)
        self.__last.insert_current_node_at_address(new_node)
        self.__last = new_node

    def front(self):
        return self.__head

    def back(self):
        return self.__last

    def size(self):
        self.__iterate_through_node_and_count_number_of_items()
        return self.__size

    def __iterate_through_node_and_count_number_of_items(self):
        current_node: Node = self.__head
        while current_node is not None:
            self.__size = self.__size + 1
            current_node = current_node.get_linked_node()

    def insert_at(self, node_index, data):
        self.__insert_at_a_specific_index(node_index, data)

    def __insert_at_a_specific_index(self, node_index, data):
        new_node: Node = Node(data)
        current_node: Node = self.__head
        index_counter = 0
        while current_node is not None:
            if node_index == index_counter:
                new_node.insert_current_node_at_address(current_node.get_linked_node())
                current_node.insert_current_node_at_address(new_node)
            index_counter += 1
            current_node = current_node.get_linked_node()


    def insert_at_start(self, data):
        new_node: Node = Node(data)
        current_node: Node = self.__head
        new_node.insert_current_node_at_address(current_node)
        self.__head = new_node

    def destroy_list(self):
        self.__head = None

    def delete(self, node_index):
        previous_index = node_index - 1
        current_node: Node = self.__head
        node_counter = 0
        while current_node is not None:
            if previous_index == node_counter:
                current_node.insert_current_node_at_address(current_node.get_linked_node().get_linked_node())
            node_counter += 1
            current_node = current_node.get_linked_node()

    def display(self):
        array_of_data_in_each_node = []
        current_node: Node = self.__head
        while current_node is not None:
            array_of_data_in_each_node.append((current_node.get_data()))
            current_node = current_node.get_linked_node()
        return str(array_of_data_in_each_node)

    def search(self, data):
        current_node: Node = self.__head
        while current_node is not None:
            if current_node.get_data() == data:
                return True
            current_node = current_node.get_linked_node()
