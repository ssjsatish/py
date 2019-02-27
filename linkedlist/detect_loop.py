'''
detect loop if there is any in a given linked list
'''
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def detectLoop(self, node):
        
        return True
    