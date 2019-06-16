class treeNode:
    def __init__(self, new_data):
        self.right = None
        self.left = None
        self.data = new_data
    
    def inorder(temp):
        if temp:
            inorder(temp.left):
            print(temp.data, end = ' ')
            inorder(temp.right)