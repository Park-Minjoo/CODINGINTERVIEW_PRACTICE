def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root)