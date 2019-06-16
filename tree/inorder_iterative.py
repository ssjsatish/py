class TreeNode:
    def __init__(self, new_data):
        self.left = None
        self.right = None
        self.data = new_data


def inorder_iterative(root):
    current = root
    s = []
    done = 0
    while(not done):
        if current is not None:
            s.append(current)
            current = current.left
        else:
            if(len(s)>0):
                current = s.pop()
                print(current.data,end=' ')
                current = current.right
            else:
                done = 1
root = TreeNode(1) 
root.left = TreeNode(2) 
root.right = TreeNode(3) 
root.left.left = TreeNode(4) 
root.left.right = TreeNode(5) 
  
inorder_iterative(root)
print()

            
