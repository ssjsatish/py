class TreeNode:
    def __init__(self, new_data):
        self.data = new_data
        self.left = None
        self.right = None
def getMaxWidth(root):
    maxWidth = 0
    h = height(root)
    for i in range(1, h+1):
        width = getMaxWidth(root, i)
        if width > maxWidth:
            maxWidth = width
    return maxWidth

def height(root):
    if root is None:
        return 0
    else:
        lheight = height(root.left)
        rheight = height(root.right)
    return (lheight+1) if lheight > rheight else (rheight+1)

root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 
root.right.right = TreeNode(8) 
root.right.right.left = TreeNode(6) 
root.right.right.right = TreeNode(7) 

print(getMaxWidth(root))
