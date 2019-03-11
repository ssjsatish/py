class TreeNode:
    def __init__(self, new_data):
        self.left = None
        self.right = None
        self.data = new_data
def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))

def diameter(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height =height(root.right)
    left_diameter = diameter(root.left)
    right_diameter = diameter(root.right)
    return max((left_height+right_height+1), max(right_diameter,left_diameter))

def optimzed_diameter(root):
    if root is None:
        return 0
    return 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left =TreeNode(5)
print(diameter(root))