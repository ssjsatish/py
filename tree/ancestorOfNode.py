class TreeNode:
    def __init__(self,new_data):
        self.data = new_data
        self.left = None
        self.right = None
def getAncestors(root, target):
    if root is None:
        return
    if root.data == target:
        return True
    if (getAncestors(root.left, target) or getAncestors(root.right,target)):
        print(root.data, end=' ')
        return True
    return False

root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 
root.left.left.left = TreeNode(7) 
  
getAncestors(root, 7)



