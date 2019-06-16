from sys import maxsize
def createStack():
    stack = []
    return stack

def isEmpyt(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print(item + ' pushed to stack')

def pop(stack):
    if(isEmpyt(stack)):
        return str(-maxsize - 1 )
    return stack.pop()

def printStack(stack):
    print(stack)

stack = createStack()
push(stack,str(10))
push(stack,str(20))
push(stack,str(40))
print(pop(stack)+ ' popped from stack')
printStack(stack)