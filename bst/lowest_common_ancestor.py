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

def getLCA_rec(root, a, b):
    if root is None:
        return None
    if root.data > a and root.data > b:
        return getLCA_rec(root.left, a, b)
    if root.data < a and root.data < b:
        return getLCA_rec(root.right, a, b)
    return root

def getLCA_itr(root, n1, n2):
    while root is not None:
        if root.data > n1 and root.data > n2:
            root = root.left
        elif root.data < n1 and root.data < n2:
            root = root.right
        else:
            break
    return root

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
a = 3
b = 8
ans = getLCA_rec(root, a, b )
print(ans.data)
ans = getLCA_itr(root, a, b )
print(ans.data)