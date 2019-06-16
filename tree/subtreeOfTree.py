class TreeNode:
    def __init__(self,new_data):
        self.data = new_data
        self.left = None
        self.right = None
def isIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return root1.data==root2.data and isIdentical(root1.left, root2.left) and isIdentical(root1.right,root2.right)

def isSubTree(T,S):
    if S is None:
        return True
    if T is None:
        return False
    if isIdentical(T,S):
        return True
    return isSubTree(T.left,S) or isSubTree(T.right,S)

T = TreeNode(26) 
T.right = TreeNode(3) 
T.right.right  = TreeNode(3) 
T.left = TreeNode(10) 
T.left.left = TreeNode(4) 
T.left.left.right = TreeNode(30) 
T.left.right = TreeNode(6) 

S = TreeNode(10) 
S.right = TreeNode(6) 
S.left = TreeNode(4) 
S.left.right = TreeNode(30) 
if isSubTree(T,S):
    print('YES')
else:
    print('NO')
