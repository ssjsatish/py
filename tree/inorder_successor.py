class TreeNode:
    def __init__(self,new_data):
        self.right = None
        self.left  = None
        self.data = new_data

def inorder_successor(root, node):
    if node.right is not None:
        return minValue(node.right)
    p = node.parent()
