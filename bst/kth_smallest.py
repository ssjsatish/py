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
    s, cur, rank = [], root, 0
    while s or cur:
        if cur:
            s.append(cur)
            cur = cur.left
        else:
            cur = s.pop()
            rank = rank + 1
            if rank == k:
                return cur.data
            cur = cur.right
    return float("-inf")

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
print('1st smallest:  ', kth_smallest(root, 1))
print('2nd smallest:  ', kth_smallest(root, 2))
print('3rd smallest:  ', kth_smallest(root, 3))
print('4th smallest:  ', kth_smallest(root, 4))
print('5th smallest:  ', kth_smallest(root, 5))
print('6th smallest:  ', kth_smallest(root, 6))
print('7th smallest:  ', kth_smallest(root, 7))
print('8th smallest:  ', kth_smallest(root, 8))
print('9th smallest:  ', kth_smallest(root, 9))
print('10th smallest: ', kth_smallest(root, 10))
print('11th smallest: ', kth_smallest(root, 11))
print('12th smallest: ', kth_smallest(root, 12))
print('13th smallest: ', kth_smallest(root, 13))
print('14th smallest: ', kth_smallest(root, 14))
print('15th smallest: ', kth_smallest(root, 15))
print('16th smallest: ', kth_smallest(root, 16))
print('0th smallest:  ', kth_smallest(root, 0))