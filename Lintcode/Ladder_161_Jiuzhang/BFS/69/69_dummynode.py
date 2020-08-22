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
        # DummyNode
        if not root:
            return []

        queue = collections.deque([root, None])
        results, level = [], []

        while queue:
            node = queue.popleft()
            if node is None:
                results.append(level)
                level = []
                if queue:
                    # 空了就不加none了
                    queue.append(None)
                continue
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return results