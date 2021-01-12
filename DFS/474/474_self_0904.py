"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """

    def lowestCommonAncestorII(self, root, A, B):

        visited = set()
        while A is not root:
            visited.add(A)
            A = A.parent

        while B is not root:
            # not is in!!!!!
            if B in visited:
                return B
            visited.add(B)
            B = B.parent

        return root
