def preorder(root):
    if root in None:
        return

    print(root)
    preorder(root.left)
    preorder(root.right)