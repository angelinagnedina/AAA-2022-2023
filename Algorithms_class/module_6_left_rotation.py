class TreeNode:
    def __init__(self, parent, key: int):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent


def dfs(node: TreeNode, preorder_keys: list) -> list:
    """
    Поиск в глубину.

    :param node: нода, из которой начинается поиск,
    :param preorder_keys: список уже пройденных вершин,
    :return: список, хранящий вершины в порядке обхода.
    """
    preorder_keys.append(node.key)

    if node.left:
        preorder_keys = dfs(node.left, preorder_keys)
    if node.right:
        preorder_keys = dfs(node.right, preorder_keys)

    return preorder_keys


def find_and_left_rotate(preorder_keys: list, key: int) -> list:
    """
    Осуществляет левое вращение поддерева, если возможно.

    :param preorder_keys: список вершин в дереве,
    :param key: ключ вершины, по которой осуществляется вращение,
    :return: обновлённый список вершин после вращения.
    """
    root = TreeNode(None, preorder_keys[0])

    # Строим дерево
    for el in preorder_keys[1:]:
        new_root = root

        while True:
            if el < new_root.key:
                if new_root.left is None:
                    child = TreeNode(new_root, el)
                    new_root.left = child
                    break

                new_root = new_root.left
            else:
                if new_root.right is None:
                    child = TreeNode(new_root, el)
                    new_root.right = child
                    break

                new_root = new_root.right

    # Ищем вершину, по которой будет происходить левое вращение
    curr_node = root

    while curr_node.key != key:
        if curr_node.key > key:
            curr_node = curr_node.left
        else:
            curr_node = curr_node.right

    # Проверка на возможность левого вращения
    if curr_node.right:
        child = curr_node.right
        child.parent = curr_node.parent

        if child.parent is None:
            root = child
        elif child.parent.key > child.key:
            child.parent.left = child
        else:
            child.parent.right = child

        curr_node.right = child.left if child.left else None
        curr_node.parent = child
        child.left = curr_node

    # Обход дерева
    return dfs(root, [])


def solution():
    preorder_keys = list(map(int, input().split()))
    key = int(input())
    preorder_keys_after_rotate = find_and_left_rotate(preorder_keys, key)
    print(' '.join(map(str, preorder_keys_after_rotate)))


if __name__ == '__main__':
    solution()
