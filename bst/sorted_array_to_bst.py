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

arr = [1,2,3,4,5,6,7,8,9]
root = sorted_array_to_bst(arr)
preorder(root)