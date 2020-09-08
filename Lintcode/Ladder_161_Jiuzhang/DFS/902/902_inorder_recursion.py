"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def helper(self, root, k, traverse):
        if root:
            self.helper(root.left, k, traverse)
            traverse.append(root.val)
            self.helper(root.right, k, traverse)

        if len(traverse) >= k:
            return traverse[k - 1]

    def kthSmallest(self, root, k):
        res = self.helper(root, k, [])
        return res