class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def findPredSucc(root, data):
    if root is None:
        return  
    if root.data == data:
        if root.left is not None:
            temp = root.left
            while(temp.right):
                temp = temp.right
            findPredSucc.predecessor = temp
        if root.right is not None:
            temp = root.right
            while(temp.left):
                temp = temp.left
            findPredSucc.successor = temp
        return
    if root.data > data:
        findPredSucc.successor = root
        findPredSucc(root.left, data)
    else:
        findPredSucc.predecessor = root
        findPredSucc(root.right, data)

def insert(root, data):
    if root is None:
        return TreeNode(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

data = 65
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)
findPredSucc.predecessor = None
findPredSucc.successor = None
findPredSucc(root,data)
inorder(root)
print()
if findPredSucc.predecessor is not None:
    print('Predecessor is : ', findPredSucc.predecessor.data)
else:
    print('No predecessor')
if findPredSucc.successor is not None:
    print('successor is :', findPredSucc.successor.data)
else:
    print('No Successor')
