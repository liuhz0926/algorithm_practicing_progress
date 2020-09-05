"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """

    def findSubtree(self, root):
        min_sum, min_root, _ = self.divideConquer(root)

        return min_root

    def divideConquer(self, root):
        if not root:
            return float('inf'), None, 0

        left_min_sum, left_root, left_sum = self.divideConquer(root.left)
        right_min_sum, right_root, right_sum = self.divideConquer(root.right)

        root_sum = left_sum + right_sum + root.val

        if left_min_sum == min(left_min_sum, right_min_sum, root_sum):
            return left_min_sum, left_root, root_sum
        if right_min_sum == min(left_min_sum, right_min_sum, root_sum):
            return right_min_sum, right_root, root_sum
        return root_sum, root, root_sum

