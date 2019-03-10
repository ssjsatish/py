class TreeNode:
    def __init__(self,new_data):
        self.data = new_data
        self.left = None
        self.right = None
    
def height(root):
    if root is None:
        return 0
    else:
        left_height = height(root.left)
        right_height = height(root.right)
        if left_height > right_height:
            return left_height+1
        else:
            return right_height +1
            
def printLevelOrder( root ):
    h = height(root)
    for i in range(1, h+1):
        printLevel(root, i )
    print()

def printLevel(root, level):
    if root is None:
        return 
    if level == 1:
        print(root.data, end = ' ')
    elif level >= 1:
        printLevel(root.left, level-1)
        printLevel(root.right, level-1 )

#TreeNode node = TreeNode()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
printLevelOrder(root)