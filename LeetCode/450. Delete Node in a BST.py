class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'TreeNode({self.val}, {self.left}, {self.right})'


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        # first search for the node
        if root is None: return None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:  # root.val == key
            # no right branch
            if root.right is None: return root.left
            # no left branch
            elif root.left is None: return root.right
            parents = [root, root]
            candidates = [root.left, root.right]
            # find next smallest or next largest node
            while (candidates[0].right is not None or candidates[1].left is not None):
                # find largest value < key
                if candidates[0].right is not None:
                    parents[0] = candidates[0]
                    candidates[0] = candidates[0].right
                # find smallest value > key
                if candidates[1].left is not None:
                    parents[1] = candidates[1]
                    candidates[1] = candidates[1].left
            # is smallest value bigger than key closer to key than biggest value smaller than key?
            is_right_side = candidates[0].val + candidates[1].val - 2 * key > 0
            # not possible to be None, None since that is checked before the while loop
            root.val = candidates[is_right_side].val
            if is_right_side:
                if root.val == parents[1].val: parents[1].right = candidates[1].right
                else: parents[1].left = candidates[1].right
            else:
                if root.val == parents[0].val: parents[0].left = candidates[0].left
                else: parents[0].right = candidates[0].left
        return root
