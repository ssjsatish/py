class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    # add a node to the front of the list
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    

