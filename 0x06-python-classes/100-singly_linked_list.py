#!/usr/bin/python3
"""module 100-singly_linked_list.py"""


class Node:
    """defines a node of a singly linked list by"""

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__next_node = value

    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def next_node(self, value):
        if value not in Node.data:
            pass


class SinglyLinkedList:
    """defines a singly linked list by"""

    def __init__(self, head):
        self.__head = head
