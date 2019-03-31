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

def getLowestCommonAncestor(root, a, b):
    
    return 0

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
ans = getLowestCommonAncestor(root, a, b )
print(ans)