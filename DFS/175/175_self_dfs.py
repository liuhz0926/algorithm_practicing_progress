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

    def invertBinaryTree(self, root):
        if not root:
            return

        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)

        root.left, root.right = root.right, root.left

        return

    # 九章答案：
    def invertBinaryTree(self, root):
        # write your code here
        if not root:
            return None

        left_node = self.invertBinaryTree(root.left)
        right_node = self.invertBinaryTree(root.right)

        root.left, root.right = right_node, left_node

        return root