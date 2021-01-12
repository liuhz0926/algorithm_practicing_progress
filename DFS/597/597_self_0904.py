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
    @return: the root of the maximum average of subtree
    """

    def findSubtree2(self, root):
        max_avg, max_root, sum, count = self.divideConquer(root)

        return max_root

    def divideConquer(self, root):
        if not root:
            return -float('inf'), None, 0, 0

        left_max_avg, left_root, left_sum, left_count = self.divideConquer(root.left)
        right_max_avg, right_root, right_sum, right_count = self.divideConquer(root.right)

        root_sum = left_sum + right_sum + root.val
        root_count = left_count + right_count + 1
        root_avg = root_sum / root_count

        if left_max_avg == max(left_max_avg, right_max_avg, root_avg):
            return left_max_avg, left_root, root_sum, root_count
        if right_max_avg == max(left_max_avg, right_max_avg, root_avg):
            return right_max_avg, right_root, root_sum, root_count
        return root_avg, root, root_sum, root_count