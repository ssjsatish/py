class TreeNode:
    def __init__(self, new_data):
        self.data = new_data
        self.left = None
        self.right = None

#insert the nodes in the tree, this insertion is not self balanced
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

#Inorder traversal of the tree i.e. Left, Node then Right(L N R)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

# get the leftmost node's value which is smallest
def minVal(root):
    current = root
    while(current.left is not None):
        current = current.left
    return current.data
    

# method to search any element in the tree
def search(root, key):
    if root is None or root.data == key:
        return root
    if root.data < key:
        return search(root.left, key)
    return search(root.right,key)

# print the node's value from left to right per level from 0 to height of the tree
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

def deleteNode(root, val):
    if root is None:
        return root
    # if the node to be deleted lies in the left subtree of the original tree
    if val < root.data:
        root.left = deleteNode(root.left, val)
    # if the node to be deleted lies in the right subtree of the original tree
    elif(val > root.data):
        root.right = deleteNode(root.right, val)
    # if the node to be deleted is the root 
    else:
        # node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minVal(root.right)
        root.data = temp.data
        root.right = deleteNode(root.right, temp.data)
    return root

root = TreeNode(9)
insert(root, TreeNode(5))
insert(root, TreeNode(7))
insert(root, TreeNode(6))
insert(root, TreeNode(8))
insert(root, TreeNode(3))
insert(root, TreeNode(4))
insert(root, TreeNode(2))
insert(root, TreeNode(13))
insert(root, TreeNode(11))
insert(root, TreeNode(10))
insert(root, TreeNode(12))
insert(root, TreeNode(15))
insert(root, TreeNode(14))
insert(root, TreeNode(16))
print('Inorder traversal: ', end='')
inorder(root)
print()
print('Level order traversal: ', end='')
printLevelOrder(root)
print()
root = deleteNode(root, 15)
inorder(root)