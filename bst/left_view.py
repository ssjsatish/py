class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def leftView(root):
    return None



root = TreeNode(9)
root.left = TreeNode(7)
root.left.left = TreeNode(6)
root.left.right = TreeNode(8)
root.right = TreeNode(11)
root.right.left = TreeNode(10)
root.right.right = TreeNode(12)
