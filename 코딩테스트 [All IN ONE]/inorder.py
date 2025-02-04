def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root)
    inorder(root.right)