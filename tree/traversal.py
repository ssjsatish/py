class TreeNode:
    def __init__(self,new_data):
        self.data = new_data
        self.left = None
        self.right = None
    
def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        if left_height > right_height:
            return left_height+1
        else:
            return right_height +1
            
def printLevelOrder( root ):
    h = height(root)
    for i in range(1, h+1):
        printLevel(root, i )
    print()

def printLevel(root, level):
    if root is None:
        return 
    if level == 1:
        print(root.data, end = ' ')
    elif level >= 1:
        printLevel(root.left, level-1)
        printLevel(root.right, level-1 )
def printLevelOrderQueue(root):
    if root is None:
        return
    q = []
    q.append(root)
    while(len(q) > 0):
        print(q[0].data, end = ' ')
        node = q.pop(0)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)
    

def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)
    

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end = ' ')
    


#TreeNode node = TreeNode()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
printLevelOrder(root)
printLevelOrderQueue(root)
print()
inorder(root)
print()
preorder(root)
print()
postorder(root)
print()
