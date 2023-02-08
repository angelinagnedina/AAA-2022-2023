from heapq import heapify, heappush, heappop


def bfs(graph: dict, start_node: int, finish_node: int) -> list:
    """
    Поиск в ширину (с детекцией дубликатов).

    :param graph: граф в формате adjacency list,
    :param start_node: ключ начальной вершины,
    :param finish_node: ключ конечной вершины,
    :return: кратчайший путь.
    """
    que = [(0, start_node, start_node)]
    heapify(que)
    parents = {}  # key - id вершины в графе, value - id родителя в кратчайшем пути от
    # start_node до key

    while len(que):
        level, node_id, parent = heappop(que)

        # Детекция дубликатов
        if parents.get(node_id) is not None:
            continue

        parents[node_id] = parent

        if node_id == finish_node:
            break

        for n in graph[node_id]:
            heappush(que, (level + 1, n, node_id))

    # Восстанавливаем путь
    path = []
    last_node = finish_node
    while last_node != start_node:
        path.append(last_node)
        last_node = parents[last_node]

    return path[::-1]


if __name__ == '__main__':
    id_analytics = None
    id_algorithm = None
    page_names = {}
    graph = {}

    # Путь до файла с названиями страниц
    filename1 = "../Files_with_data/simple_english_wiki_pages.csv"
    # Сохраняем соотношения между id и названием страницы
    with open(filename1) as f:
        for line in f.readlines()[1:]:
            page_id, page_title = line.rstrip().split(',')[1:3]
            page_names[int(page_id)] = page_title
            
            if page_title == 'Analytics':
                id_analytics = int(page_id)
            if page_title == 'Algorithm':
                id_algorithm = int(page_id)

    # Проверка на наличие страниц
    assert id_algorithm and id_analytics, 'No such pages'

    # Путь до файла со ссылками
    filename2 = "../Files_with_data/simple_english_wiki_pagelinks.csv"
    # Создаём взвешенный граф в формате adjacency list
    with open(filename2) as f:
        for line in f.readlines()[1:]:
            data = line.rstrip().split(',')
            page_from, page_to = int(data[1]), int(data[-1])

            if graph.get(page_from) is None:
                graph[page_from] = [page_to]
            else:
                graph[page_from].append(page_to)

            if graph.get(page_to) is None:
                graph[page_to] = []

    path = bfs(graph, id_analytics, id_algorithm)
    print(len(path))  # Длина кратчайшего пути, задача 1
    print(page_names.get(path[-2]))  # Название страницы, ссылающейся на Algorithms, задача 2
