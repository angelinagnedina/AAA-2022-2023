class TreeNode:
    def __init__(self, parent, key: int):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent


def dfs(node: TreeNode, preorder_keys: list):
    preorder_keys.append(node.key)

    if node.left:
        preorder_keys = dfs(node.left, preorder_keys)
    if node.right:
        preorder_keys = dfs(node.right, preorder_keys)

    return preorder_keys


def find_and_left_rotate(preorder_keys: list, key: int):
    root = TreeNode(None, preorder_keys[0])

    for el in preorder_keys[1:]:
        new_root = root

        while True:
            if el < new_root.key:
                if new_root.left:
                    new_root = new_root.left
                else:
                    child = TreeNode(new_root, el)
                    new_root.left = child
                    break
            else:
                if new_root.right:
                    new_root = new_root.right
                else:
                    child = TreeNode(new_root, el)
                    new_root.right = child
                    break

    curr_node = root

    while curr_node.key != key:
        if curr_node.key > key:
            curr_node = curr_node.left
        else:
            curr_node = curr_node.right

    if curr_node.right:
        child = curr_node.right
        child.parent = curr_node.parent

        if child.parent:
            if child.parent.key > child.key:
                child.parent.left = child
            else:
                child.parent.right = child
        else:
            root = child

        if child.left:
            curr_node.right = child.left
        else:
            curr_node.right = None

        curr_node.parent = child
        child.left = curr_node

        return dfs(root, [])
    else:
        return preorder_keys


def solution():
    preorder_keys = list(map(int, input().split()))
    key = int(input())
    preorder_keys_after_rotate = find_and_left_rotate(preorder_keys, key)
    print(' '.join(map(str, preorder_keys_after_rotate)))


if __name__ == '__main__':
    solution()
