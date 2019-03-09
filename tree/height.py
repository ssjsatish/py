class treeNode:
    def __init__(self,new_data):
        self.data = new_data
        self.left = None
        self.right - None
    
    def inorder( temp ):
        if not temp:
            return
        inorder(temp.left)
        print(temp.data, end = ' ')
        inorder(temp.right)

    def insert(temp, new_data):
        q = []
        q.append(temp)
        while(len(q)):
            temp = q[0]
            q.pop(0)
            if (not temp.left):
                temp.left = treeNode(new_data)
                break
            else:
                q.append(temp.left)
            if(
                
            )