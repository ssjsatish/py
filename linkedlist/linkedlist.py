class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def add_to_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def insert_after_node(self,prev_node,new_data):
        #check if given exists or not?
        if prev_node is None:
            print("given node doesn't exist. exiting the program")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    def add_node_at_end(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next
        print()
if __name__=='__main__':
    llist = LinkedList()
    llist.add_to_front(6)
    llist.print_list()
    llist.add_to_front(5)
    llist.print_list()
    llist.add_node_at_end(7)
    llist.print_list()
    llist.insert_after_node(llist.head.next.next, 10)
    llist.print_list()
