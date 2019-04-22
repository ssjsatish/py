class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=' ')
        preorder(root.left)
        preorder(root.right)


def create_balanced_bst(arr):
    # print("Balancing tree now: ")
    if not arr:
        return None
    mid = (len(arr))//2
    root = TreeNode(arr[mid])
    root.right = create_balanced_bst(arr[:mid])
    root.left = create_balanced_bst(arr[mid+1:])
    return root

def bst_to_balanced_bst(root):
    # print('Inorder traversal: ')
    # inorder(root)
    # print()
    s, cur,a = [], root, []
    while s or cur:
        if cur:
            s.append(cur)
            a.append(cur.data)
            cur = cur.left
        else:
            cur = s.pop()
            cur = cur.right
    # print('sorted array:\n')
    # print(a)
    temp = create_balanced_bst(a)
    return temp
def printLevelOrderQueue(root):
    if root is None:
        return
    q = []
    q.append(root)
    while(len(q) > 0):
        print(q[0].data, end = ' ')
        node = q.pop(0)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)

root = TreeNode(9)
root.left = TreeNode(8)
root.left.left = TreeNode(7)
root.left.left.left = TreeNode(6)
root.left.left.left.left = TreeNode(5)
root.left.left.left.left.left = TreeNode(4)
printLevelOrderQueue(root)
# preorder(root)
print()
# inorder(root)
print()
print('\nCalling method to balance the tree: \n')
root = bst_to_balanced_bst(root)
# preorder(root)
printLevelOrderQueue(root)
# print()
# inorder(root)
# print(root.data)
# print(root.left.data)
# print(root.right.data)
# print(root.left.right.data)
# print(root.right.left.data)
# print(root.right.right.data)
