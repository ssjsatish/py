class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)
    return root
def kth_smallest(root, k):
    i = 0
    ans = 0
    if root:
        kth_smallest(root.left, k)
        #print(root.data, end=' ')
        i = i + 1
        if i == k:
            ans = root.data
        kth_smallest(root.right, k)
    return ans
root = TreeNode(9)
insert(root, TreeNode(5))
insert(root, TreeNode(7))
insert(root, TreeNode(6))
insert(root, TreeNode(8))
insert(root, TreeNode(3))
insert(root, TreeNode(4))
insert(root, TreeNode(2))
insert(root, TreeNode(13))
insert(root, TreeNode(11))
insert(root, TreeNode(10))
insert(root, TreeNode(12))
insert(root, TreeNode(15))
insert(root, TreeNode(14))
insert(root, TreeNode(16))
ans = kth_smallest(root, 1)
print(ans)