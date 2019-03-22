class TreeNode:
    def __init__(self, new_data):
        self.data = new_data
        self.left = None
        self.right = None
        self.nextRight = None
    
    def __str__(self):
        return '{}'.format(self.data)

def printLevelByLevel(root):
    if root:
        temp = root
        while temp:
            print('{}'.format(temp.data), end=' ')
            temp = temp.nextRight
        print()
        if root.left:
            printLevelByLevel(root.left)
        else:
            printLevelByLevel(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def connect(root):
    # set nextRight of all nodes of a tree
    q = []
    q.append(root)
    #None marker to represent the end of current level
    q.append(None)
    # do level order for tree using None marker
    while q:
        tmp = q.pop()
        if tmp:
            # next element in the q represents the next node at current level
            tmp.nextRight = q[0]
            # push left and right children of current node
            if tmp.left:
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.rightht)
        elif q:
            q.append(None)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right =TreeNode(5)
connect(root)
print(root.left.left.nextRight.data)