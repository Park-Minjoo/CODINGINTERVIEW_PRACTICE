from _collections import deque

def levelOrderTraversal(root):
    # visited = []
    max_depth = 0
    if root in None:
        return max_depth

    q = deque()
    q.append((root, 1))

    while q:
        cur_node, cur_depth = q.popleft()
        # visited.append(cur_node.value)
        max_depth = max(max_depth, cur_depth)
        if cur_node.left:
            q.append((cur_node.left, cur_depth+1))
        if cur_node.right:
            q.append((cur_node.right, cur_depth+1))
    return max_depth