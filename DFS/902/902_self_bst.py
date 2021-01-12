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
    @param k: the given k
    @return: the kth smallest element in BST
    """

    def kthSmallest(self, root, k):
        # use binary serach interator to pop stack k-1 times and return the last node in the stack

        stack = []
        self.add_all_left_nodes(root, stack)

        for _ in range(k - 1):
            node = stack.pop()
            if node.right:
                self.add_all_left_nodes(node.right, stack)

            # if stack is empty but not reach k - 1 times
            if not stack:
                return None

        return stack[-1].val

    def add_all_left_nodes(self, node, stack):
        while node:
            stack.append(node)
            node = node.left
