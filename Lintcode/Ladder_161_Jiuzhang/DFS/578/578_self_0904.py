"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """

    def lowestCommonAncestor3(self, root, A, B):
        hasA, hasB, lca = self.divideConquer(root, A, B)
        if hasA and hasB:
            return lca
        return None

    def divideConquer(self, root, A, B):
        if not root:
            return False, False, None

        left_hasA, left_hasB, left_lca = self.divideConquer(root.left, A, B)
        right_hasA, right_hasB, right_lca = self.divideConquer(root.right, A, B)

        hasA = left_hasA or right_hasA or root == A
        hasB = left_hasB or right_hasB or root == B

        if root == A or root == B:
            return hasA, hasB, root

        # 还是需要用left lca来判断！两边是否有没有lca。同时都有才是真的有。
        # hasA hasB只是来判断有没有的
        if left_lca and right_lca:
            return hasA, hasB, root
        if left_lca:
            return hasA, hasB, left_lca
        if right_lca:
            return hasA, hasB, right_lca
        # 都没有
        return hasA, hasB, None
