"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root, target):

        if not root:
            return None

        if target < root.val:
            result = self.closestValue(root.left, target)
        else:
            result = self.closestValue(root.right, target)

        if result:
            if abs(result - target) < abs(root.val - target):
                return result
            else:
                return root.val


        else:
            return root.val

