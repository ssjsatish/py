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
    def delete_last(self):
        if(self.head is None):
            return None
        if(self.head.next is None):
            self.head = None
            return None
        second_last = self.head
        while(second_last.next.next is not None):
            second_last = second_last.next
        last = second_last.next
        second_last.next = None
        last = None
        return self.head
    def remove_node_from_position(self,position):
        if(self.head is None):
            return None
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp =None
            return self.head
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break
            
if __name__=='__main__':
    llist = LinkedList()
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    #llist.print_list()
    #llist.delete_front()
    llist.print_list()
    llist.delete_last()
    llist.print_list()
    llist.delete_last()
    llist.print_list()

