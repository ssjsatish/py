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
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data,' -> ', end=' ')
            temp = temp.next
        print('None')
    # delete the front node
    def delete_front(self):
        temp = self.head
        self.head = temp.next
        temp = None
if __name__=='__main__':
    llist = LinkedList()
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.print_list()
    llist.delete_front()
    llist.print_list()
    
    

