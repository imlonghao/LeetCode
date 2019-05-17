class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0
        c = root.val if L <= root.val <= R else 0
        if root.val >= L:
            c += self.rangeSumBST(root.left, L, R)
        if root.val <= R:
            c += self.rangeSumBST(root.right, L, R)
        return c
