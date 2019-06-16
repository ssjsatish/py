class treeNode:
    def __init__(self,new_data):
        self.left = None
        self.right = None
        self.data = new_data
    
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end = ' ')
    inorder(root.right)

def insert(root, new_data):
    q = []
    q.append(root)
    while(len(q)):
        node = q[0]
        q.pop(0)
        if not node.left:
            node.left = treeNode(new_data)
            break
        else:
            q.append(node)
        if not node.right:
            node.right = treeNode(new_data)
            break
        else:
            q.append(root.right)
if __name__ == '__main__': 
    root = treeNode(10)  
    root.left = treeNode(11)  
    root.left.left = treeNode(7)  
    root.right = treeNode(9)  
    root.right.left = treeNode(15)  
    root.right.right = treeNode(8)  
  
    print("Inorder traversal before insertion:", end = " ") 
    inorder(root)  
  
    key = 12
    insert(root, key)  
  
    print()  
    print("Inorder traversal after insertion:", end = " ") 
    inorder(root) 
