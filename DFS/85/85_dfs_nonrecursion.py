"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        if not root:
            return node

        curt = root
        while curt != node:
            if node.val < curt.val:

                if curt.left is None:
                    curt.left = node

                curt = curt.left
            else:

                if curt.right is None:
                    curt.right = node

                curt = curt.right

        return root

