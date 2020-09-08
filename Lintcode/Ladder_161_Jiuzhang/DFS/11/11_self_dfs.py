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
        if not root or k1 > k2:
            return []

        stack = []
        while root:
            stack.append(root)
            root = root.left

        result = []
        while stack and stack[-1].val <= k2:
            node = stack.pop()
            if k1 <= node.val <= k2:
                result.append(node.val)
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        return result