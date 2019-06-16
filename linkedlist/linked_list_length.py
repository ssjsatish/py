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
    def getLength(self):
        temp = self.head
        count = 0
        while(temp):
            count +=1
            temp = temp.next
        return count
    def lengthRecursive(self,node):
        if(not node):
            return 0
        else:
            return 1+self.lengthRecursive(node.next)
if __name__ == '__main__':
    llist = LinkedList()
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    print(llist.getLength())
    print(llist.lengthRecursive(llist.head))