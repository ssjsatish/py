class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
    return root

def minVal(root):
    current = root
    while(current.left is not None):
        current = current.left
    return current.data

def maxVal(root):
    current = root
    while(current.right is not None):
        current = current.right
    return current.data

def isBST(root):
    if root is None:
        return True
    if root.left is not None and maxVal(root.left) > root.left.data:
        return False
    if root.right is not None and minVal(root.right) < root.right.data:
        return False
    if(not isBST(root.left) or not isBST(root.right)):
        return False
    return True

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def printLevelOrder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while(len(queue)>0):
        print(queue[0].data, end=' ')
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

def isBST_iterative(root):
    s, cur = [], root
    while s or cur:
        if cur:
            s.append(cur)
            cur =cur.left
        else:
            cur = s.pop()
            cur = cur.right
    return s 

def is_sorted(a):
    flag = 0
    if(all(a[i] <= a[i + 1] for i in range(len(a)-1))):
        flag = 1
    return True if flag==1 else False

root = TreeNode(9)
root = insert(root, TreeNode(5))
root = insert(root, TreeNode(7))
root = insert(root, TreeNode(6))
root = insert(root, TreeNode(8))
root = insert(root, TreeNode(3))
root = insert(root, TreeNode(4))
root = insert(root, TreeNode(2))
root = insert(root, TreeNode(13))
root = insert(root, TreeNode(11))
root = insert(root, TreeNode(10))
root = insert(root, TreeNode(12))
root = insert(root, TreeNode(15))
root = insert(root, TreeNode(14))
root = insert(root, TreeNode(16))
print('Inorder traversal: ', end='')
a  = isBST_iterative(root)
print()
print('Level order traversal: ', end=' ')
printLevelOrder(root)
print()
# following if else statement is wrong.
if isBST(root):
    print('This is BST')
else:
    print('Its not a BST')
# correct code using sort checks
if is_sorted(a):
    print('BST')
else:
    print('NOT BST')
# correct code using sorted method available in Python
if a == sorted(a):
    print('BST')
else:
    print('NOT BST')
