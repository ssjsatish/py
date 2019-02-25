class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def deleteNode(self, key):
        temp = self.head
        # if head node itself is having data
        if (temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return
        # start search
        while(temp is not None):
            if temp.data==key:
                break
            prev = temp
            temp = temp.next
        # if key is not found in the list
        if(temp==None):
            return
        prev.next = temp.next
        temp = None
        
        
