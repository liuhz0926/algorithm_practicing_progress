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
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def lowestCommonAncestor(self, root, A, B):
        # 如果ab都在，return lca, 如果刚汇合，lca就是当前root
        # 如果只有一边在有一个a或者一个b，return这个a或者b
        # 如果两个都在一边（其实和上面一条一样），return lca。所以就是return 当前的result
        # ab都不在，return none

        if not root:
            return None

        if root == A or root == B:
            return root

        left_lca = self.lowestCommonAncestor(root.left, A, B)
        right_lca = self.lowestCommonAncestor(root.right, A, B)

        # A 和 B 在左右一边一个 （左右都有）
        if left_lca and right_lca:
            return root
        # 只有左边有，（都在或者只有一个，return当前的这一个就可以了）
        if left_lca:
            return left_lca
        # 右子树有一个点或者右子树右lca
        if right_lca:
            return right_lca

        # 两边都没有ab或者lca
        return None
