class TreeNode:
    def __init__(self, new_data):
        self.data = new_data
        self.left = None
        self.right = None


def getMaxWidth(root):
    if root is None:
        return 0
    q = []
    maxWidth = 0
    q.append(root)
    while(len(q)>0):
        count = len(q)
        maxWidth = max(count,maxWidth)
        while(count is not 0):
            count = count - 1
            temp = q[-1]
            q.pop()
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
    return maxWidth

root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 
root.right.right = TreeNode(8) 
root.right.right.left = TreeNode(6) 
root.right.right.right = TreeNode(7)  
print(getMaxWidth(root))
print()