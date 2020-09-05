"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def flatten(self, root):

        self.connect_left_to_right(root)

        return

    def connect_left_to_right(self, root):
        if not root:
            return None

        left_last = self.connect_left_to_right(root.left)
        right_last = self.connect_left_to_right(root.right)

        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None

        # 左边最后一个 接root的右child。但是我们为什么当前这个root的funciton要返回right last优先呢，
        # 因为这个right last是这个树的最后一个，他要接的是root的parent（如果root是left child）这个parent的right。
        return right_last or left_last or root 