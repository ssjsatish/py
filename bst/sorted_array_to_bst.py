class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def sorted_array_to_bst(arr):
    if not arr:
        return None
    mid = (len(arr))//2
    root = TreeNode(arr[mid])
    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid+1:])
    return root

def preorder(root):
    if root:
        print(root.data,end=' ')
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)
    
def printlevelorder(root):
    if root is None:
        return
    queue = []
    queue.append(root)
    while(len(queue)>0):
        print(queue[0].data, end=' ')
        node = queue.pop(0)
        if node.left is not None:
            queue.append(node.left)
        if node.rightP is not None:
            queue.append(node.right)

arr = [1,2,3,4,5,6,7,8,9]
root = sorted_array_to_bst(arr)
print('Preorder: ', end=' ')
preorder(root)
print('\nInorder: ', end=' ')
inorder(root)
print('\nLevelOrder', end=' ')
printlevelorder(root)
print()