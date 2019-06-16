class TreeNode:
    def __init__(self, new_data):
        self.data = new_data
        self.left = None
        self.right = None
def printKDistant(root, k):
    if root is None:
        return
    if k==0:
        print(root.data, end=' ')
    else:
        printKDistant(root.left, k-1)
        printKDistant(root.right, k-1)
root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 
root.right.left = TreeNode(8) 
  
printKDistant(root, 2) 
print()