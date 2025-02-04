class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def LCA(self, root, p, q):
        if root is None:
            return None

        left = self.LCA(root.left, p, q)
        right = self.LCA(root.right, p, q)

        if root == p or root == q:
            return root
        elif left and right:
            return root
        return left or right

    LCA([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 6, 4)