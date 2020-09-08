"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):

        isBST, min, max = self.divideConquer(root)

        return isBST

    def divideConquer(self, root):
        if not root:
            return True, None, None

        leftIsBST, leftMin, leftMax = self.divideConquer(root.left)
        rightIsBST, rightMin, rightMax = self.divideConquer(root.right)

        if not leftIsBST or not rightIsBST:
            return False, None, None

        if leftMax and leftMax >= root.val:
            return False, None, None
        if rightMin and rightMin <= root.val:
            return False, None, None

        rootMin = leftMin if leftMin else root.val
        rootMax = rightMax if rightMax else root.val

        return True, rootMin, rootMax
