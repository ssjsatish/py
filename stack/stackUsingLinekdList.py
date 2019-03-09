class StackNode:
    def __init__(self, new_data):
        self.next = None
        self.data = new_data
    
class Stack:
    def __init__(self):
        self.root = None
    
    def isEmpty(self):
        return True if self.root is None else False
    
    def push(self, new_data):
        newNode = StackNode(new_data)
        newNode.next = self.root
        print(new_data + ' pushed to stack')

    def pop(self):
        if ( self.isEmpty() ):
            return float('-inf')
        temp = self.root
        self.root = self.root.next
        poped = temp.data
        return popped

    def peek(self):
        if self.isEmpty():
            return float('-inf')
        return self.root.data

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print(stack.pop() + ' is popped from the stack')
print('Top element is ', stack.peek())



