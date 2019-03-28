class TreeNode:
    def __init__(self, new_data):
        self.left = None
        self.right = None
        self.data = new_data
    
def tree_left_view(root):
    if root is None:
        return
    else:
        return root.data


root = TreeNode(5)
