"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import collections


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        # 单队列
        if root is None:
            return []

        queue = collections.deque([root])
        results = []
        while queue:
            level = []
            for _ in range(len(queue)):
                # queue里每一个node, 因为要pop，所以比如用长度循环
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            results.append(level)

        return results