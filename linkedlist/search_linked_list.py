'''
given a key and a linked list. Check if the key is present in the list or not
'''
class Node:
    def __init__(self, new_data):
        self.next = None
        self.data = new_data

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def search(self, key):
        if(self.head is None):
            return False
        current = self.head
        while current != None:
            if current.data == key:
                return True
            current = current.next
        return False

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data,' -> ', end=' ')
            temp = temp.next
        print('None')

if __name__=='__main__':
    llist = LinkedList()
    llist.push(9)
    llist.push(8)
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.print_list()
    print(llist.search(10))
