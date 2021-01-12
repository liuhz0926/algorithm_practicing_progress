"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        is_balanced, _ = self.divideConquer(root)

        return is_balanced

    def divideConquer(self, root):
        # 出口：空树，肯定为true，高度0
        if not root:
            return True, 0

        # 拆解，求左边是否是balanced，高度多少，求有右边
        is_left_balanced, left_height = self.divideConquer(root.left)
        is_right_balanced, right_height = self.divideConquer(root.right)
        # 整棵树的结果，先max+1
        root_height = max(left_height, right_height) + 1

        # 有一个false就不行
        if not is_left_balanced or not is_right_balanced:
            return False, root_height

        # 看两个子树差， 大于1不行
        if abs(left_height - right_height) > 1:
            return False, root_height

        return True, root_height
