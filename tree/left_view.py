class TreeNode:
    def __init__(self, new_data):
        self.left = None
        self.right = None
        self.data = new_data
    
def leftUtil(root, level, max_level):
    if root is None:
        return
    if max_level[0] < level:
        print(root.data, end=' ')
        max_level[0] = level
    leftUtil(root.left, level+1, max_level)
    leftUtil(root.right, level+1, max_level)
def printLeftView(root):
    max_level = [0]
    leftUtil(root,1,max_level)


root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(8)
root.right = TreeNode(10)
root.right = TreeNode(11)
root.right.right = TreeNode(12)
printLeftView(root)
