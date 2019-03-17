class TreeNode:
    def __init__(self, new_data):
        self.left = None
        self.right = None
        self.data = new_data

def morris_traversal(root):
    current = root
    while current is not None:
        if current.left is None:
            print(current.data, end=' ')
            

        


root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 
morris_traversal(root)
print()