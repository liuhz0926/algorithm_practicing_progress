"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """

    def __init__(self, root):
        self.stack = []
        self.add_all_left_nodes(root)

    def add_all_left_nodes(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    """
    @return: True if there has next node, or false
    """

    def hasNext(self):
        return bool(self.stack)

    """
    @return: return next node
    """

    def next(self):
        node = self.stack.pop()
        if node.right:
            self.add_all_left_nodes(node.right)
        return node