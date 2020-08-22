"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """

    def levelOrder(self, root):
        # 双队列
        if not root:
            return []

        queue_1 = [root]
        results = []

        while queue_1:
            queue_2 = []
            results.append([node.val for node in queue_1])
            for node in queue_1:
                if node.left:
                    queue_2.append(node.left)
                if node.right:
                    queue_2.append(node.right)
            queue_1 = queue_2

        return results