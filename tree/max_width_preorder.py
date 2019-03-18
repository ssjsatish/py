class TreeNode:
    def __init__(self, new_data):
        self.left = None
        self.right = None
        self.data = new_data

def getMaxWidth(root):
    h = height(root)
    count = [0]*h
    level = 0
    getMaxWidthRecurr(root, count, level)
    return getMax(count , h)

def getMaxWidthRecurr(root, count, level):
    if root is not None:
        count[level] +=1
        getMaxWidthRecurr(root.left, count, level+1)
        getMaxWidthRecurr(root.right, count, level+1)
def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        return (left_height+1) if left_height > right_height else (right_height+1)


def getMax(count, n):
    maxx = count[0]
    for i in range(1, n):
        if maxx< count[i]:
            maxx = count[i]
    return maxx


root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 
root.right.right = TreeNode(8) 
root.right.right.left = TreeNode(6) 
root.right.right.right = TreeNode(7)  
print(getMaxWidth(root))