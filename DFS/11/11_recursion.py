"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """

    def searchRange(self, root, k1, k2):
        result = []
        self.travel(root, k1, k2, result)
        return result

    def travel(self, root, k1, k2, result):
        if root is None:
            return
        # 剪枝，如果当前节点小于等于k1，不必访问左子树
        if root.val > k1:
            self.travel(root.left, k1, k2, result)
        if k1 <= root.val and root.val <= k2:
            result.append(root.val)
        # 剪枝，如果当前节点大于等于k2，不必访问右子树
        if root.val < k2:
            self.travel(root.right, k1, k2, result)