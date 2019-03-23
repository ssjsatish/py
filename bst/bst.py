class TreeNode:
    def __init__(self, new_data):
        self.data = new_data
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

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)
    

def search(root, key):
    if root is None or root.data == key:
        return root
    if root.data < key:
        return search(root.left, key)
    return search(root.right,key)
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