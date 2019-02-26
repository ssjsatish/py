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
    
    # this method is used to detect the loop 
    # in a given linked list using hashing
    def detectLoopHashMethod(self):
        h = set()
        temp = self.head
        while(temp):
            if temp in h:
                return True
            h.add(temp)
            temp = temp.next
        return False

    # detect loop in the list using floyd's cycle detection algorithm
    def detectLoopFloydMethod(self):
        slow = self.head
        fast = self.head
        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, ' -> ',end=' ')
            temp = temp.next
        print()


if __name__=='__main__':
    llist = LinkedList()
    llist.push(10)
    llist.push(20)
    llist.push(30)
    llist.push(40)
    llist.head.next.next.next.next = llist.head
    if(llist.detectLoopFloydMethod()):
        print('Has loop')
    else:
        print('Doesnt have loop')

    if(llist.detectLoopHashMethod()):
        print('list has loop')
    else:
        print('list Does not have loop')


    