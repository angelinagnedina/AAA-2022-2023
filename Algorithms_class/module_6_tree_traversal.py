class TreeNode:
    def __init__(self, parent, key: int):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent


def get_level_order_keys_and_levels(preorder_keys: list):
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

    queue = [(root, 0)]
    preorder_keys = []
    levels = []

    for el in queue:
        node, level = el
        preorder_keys.append(node.key)
        levels.append(level)

        if node.left:
            queue.append((node.left, level + 1))

        if node.right:
            queue.append((node.right, level + 1))

    return preorder_keys, levels


def solution():
    preorder_keys = list(map(int, input().split()))
    level_order_keys, levels = get_level_order_keys_and_levels(preorder_keys)
    print(' '.join(map(str, level_order_keys)))
    print(' '.join(map(str, levels)))


if __name__ == '__main__':
    solution()
