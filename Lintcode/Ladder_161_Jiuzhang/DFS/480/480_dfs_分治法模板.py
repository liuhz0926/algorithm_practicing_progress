"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """

    def binaryTreePaths(self, root):
        # 分治法
        results = []
        if not root:
            return results
        if not root.left and not root.right:
            return [str(root.val)]

        # 左子树
        for path in self.binaryTreePaths(root.left):
            results.append(str(root.val) + "->" + path)

        # 右子树
        for path in self.binaryTreePaths(root.right):
            results.append(str(root.val) + "->" + path)

        return results