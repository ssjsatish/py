class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def bst_to_balanced_bst(root):
    s, cur = [], root
     