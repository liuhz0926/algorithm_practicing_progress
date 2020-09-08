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
        if not root:
            return True

        stack = []
        while root:
            stack.append(root)
            root = root.left

        last_node = stack[-1]
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

            if stack:
                # 必须是递增关系才可以，所以不能stack小
                if last_node.val >= stack[-1].val:
                    return False
                last_node = stack[-1]

        return True
