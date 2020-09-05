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
        # 遍历法
        if not root:
            return []

        result = []
        self.dfs(root, [root], result)

        return result

    def dfs(self, node, path, result):
        if not node:
            return

        # 递归出口
        if not node.left and not node.right:
            result.append('->'.join([str(num.val) for num in path]))
            return

            # 递归拆解
        # 分治
        path.append(node.left)
        self.dfs(node.left, path, result)
        path.pop()  # 回溯

        path.append(node.right)
        self.dfs(node.right, path, result)
        path.pop()  # backtracking