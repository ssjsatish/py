class treeNode:
    def __init__(self, new_data):
        self. data  = new_data
        self.left = None
        self.right = None
    
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        print(node.data, end= ' ')
        inorder(node.right)

    def insert(node, data):
        # make a queue and start traversing the level order
        q = []
        q.append(node)
        while(len(q)):
            temp = q[0]
            q.pop(0)
            if not temp.left:
                temp.left = treeNode(data)
                break
            else:
                q.append(temp.left)
            if not temp.right:
                temp.right = treeNode(data)
                break
            else:
                q.append(temp.right)
    

