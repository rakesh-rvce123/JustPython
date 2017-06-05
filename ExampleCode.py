import os
import sys

class Node:

    def __init__(self, initValue):
        self.data = initValue
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def size(self):
        current = self.head
        count = 0;
        while current:
            count += 1
            current = current.get_next()
        return count

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def printAll(self):
        current = self.head
        while current:
            data = current.get_data()
            print(data)
            current = current.get_next()


myLinkedList = LinkedList()
myLinkedList.insert(10)
myLinkedList.insert(20)
myLinkedList.insert(30)
myLinkedList.insert(5)
myLinkedList.insert(0)
myLinkedList.printAll()


    
        
        
        

        
