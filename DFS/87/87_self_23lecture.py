"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    参考第23章ppt的内容 BST的增删改查

    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """

    def removeNode(self, root, value):
        # 因为要区分是remove root还是别的，所以加入一个dummy left为root来替换做root。这样root和其他点的情况是一样了

        dummy = TreeNode(0)
        dummy.left = root

        parent = self.findNode(dummy, root, value)
        node = None

        # 然后找到了对应的要删除的node的parent是谁了后，看他的left，right哪一个是node
        if parent.left and parent.left.val == value:
            node = parent.left
        elif parent.right and parent.right.val == value:
            node = parent.right
        else:  # 没有要删的，这里用dummy.left统一代表root，因为如果删的是root。可能也会改变
            return dummy.left

        # 找到对应的node后，根据parent和node的位置删除, return root
        self.deleteNode(parent, node)
        return dummy.left

    def findNode(self, parent, node, value):
        """
        通过分治法，找到value对应的node的parent是哪一个，因为node可以是left，right，所以需要同时记录parent和node
        """
        if not node:
            return parent
        if node.val == value:
            return parent

        if value < node.val:
            return self.findNode(node, node.left, value)
        else:
            return self.findNode(node, node.right, value)

    def deleteNode(self, parent, node):
        """
        删除，看node的位置。如果node有两个subtree，需要找右子树最小或者左子树最大进行替换。
        只有一个的话直接替换
        """
        if not node.right:  # 只有left。说明他的child刚好比他小。无论是parent比他大还是比他小。都能直接连接他的left
            # 类似删除linkedlist
            if parent.left == node:  # parent 比他大
                parent.left = node.left
            else:  # parent比他小，但是也肯定比node的left大，因为node的left在parent的leftsubtree里面
                # 而且因为不存在node right，所以可以直接连起来
                parent.right = node.left

        else:  # 存在right的情况：
            # 就要找到删除节点与右子树最小节点进行交换，由于右子树中的最小节点一定是叶子，
            # 所以直接删除并替换 （也可以找左子树的最大节点）
            temp = node.right
            temp_father = node

            # 找到右子树的最小节点和他的father上一个点
            while temp.left:
                temp_father = temp
                temp = temp.left

            # 看temp（min right subtree)是在father的哪一边，并把这个点删掉
            if temp_father.left == temp:
                temp_father.left == temp.right  # 一般是None
            else:
                temp_father.right == temp.right  # 一般是None

            # 然后替换node 通过parent来替换
            if parent.left == node:
                parent.left = temp
            else:
                parent.right = temp

            # 最后连接node的life right连接到temp的right 和 left
            temp.left = node.left
            temp.right = node.right
            # 因为parent和temp连接了且temp和剩下的subtrees连接了。
            # 虽然没有删除left right和node 的连接。但是这个tree里面已经没有node了




### 另一个方法：类似的 （上面写的那个会recursion error）

class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """

    def removeNode(self, root, value):
        dummy = TreeNode(0)
        dummy.left = root
        parent, node = self.find(root, value, dummy)
        # print(parent.val)

        if not parent:
            return root

        if parent.left is node:
            parent.left = self.remove(node)
        else:
            parent.right = self.remove(node)

        return dummy.left

    def remove(self, root):
        if root.left is None and root.right is None:
            return None

        elif root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        else:
            pre, node = root, root.right

            while node.left or node.right:
                pre = node
                if node.left:
                    node = node.left
                else:
                    node = node.right
            if pre.left is node:
                pre.left = None
            else:
                pre.right = None

            root.val = node.val
            return root

    def find(self, root, value, parent):
        if root is None:
            return None, None

        if value < root.val:
            return self.find(root.left, value, root)

        if value == root.val:
            return parent, root

        return self.find(root.right, value, root)

