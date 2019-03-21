'''
Morris traversal is based on Threaded Binary Tree
First created links to Inorder successor and then print data using these links
finally rever the changes to restore original tree
'''
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
            current = current.right
        else:
            pre = current.left
            while(pre.right is not None and pre.right!=current):
                pre = pre.right
            if pre.right is None:
                pre.right = current
                current = current.left
            else:
                pre.right = None
                print(current.data, end=' ')
                current = current.data
            

        


root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 
morris_traversal(root)
print()