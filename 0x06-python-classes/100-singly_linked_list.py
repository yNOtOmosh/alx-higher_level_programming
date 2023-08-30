#!/usr/bin/python3
"""Define classes for a singly-linked list."""

class Node:
    """
    This class represents a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node.
        __next_node (Node): The next node in the linked list.
    """
    def __init__(self, data, next_node=None):
        """
        Intanalizes a node with data and an optional next_node.

        Args:
            data (int): The data to store in the node.
            next_node (Node, optional): The next node in the linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node.

        Args:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """
        Get the next node in the linked list.
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a singly linked list.

    Attributes:
        __head: The head node of the linked list.
    """
    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the linked list.

        Args:
            value (int): The value of the new node.
        """
        new_node = Node(value)

        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
            return ("")

        current = self.__head
        while (current.next_node is not None and current.next_node.data < value):
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: A string representing the linked list.
        """
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return (result.strip())
