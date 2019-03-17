class TreeNode:
    def __init__(self, new_data):
        self.data = new_data
        self.left = None
        self.right = None
def getMaxWidth(root):
    maxWidth = 0
    h = height()