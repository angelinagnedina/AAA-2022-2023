from heapq import heapify, heappush, heappop


def djikstra(graph: dict, start_node: int, finish_node: int) -> list:
    """
    Алгоритм Дейкстры.

    :param graph: взвешенный граф в формате adjacency list,
    :param start_node: ключ начальной вершины,
    :param finish_node: ключ конечной вершины,
    :return: кратчайший путь.
    """
    open = [(0, start_node, start_node)]
    heapify(open)
    expanded = set()  # Вершины, для которых уже найден кратчайший путь из start_node
    parents = {}  # key - id вершины в графе, value - id родителя в кратчайшем пути от
    # start_node до key

    while len(open):
        weight, node, parent = heappop(open)

        # Если кратчайший путь для вершины ещё не найден
        if node not in expanded:
            expanded.add(node)
            parents[node] = parent

            if node == finish_node:
                break

            for w, neighbor in graph[node]:
                # Если кратчайший путь для соседа ещё не найден (небольшая оптимизация)
                if neighbor not in expanded:
                    heappush(open, (weight + w, neighbor, node))

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
                graph[page_from] = [(len(page_names[page_to]), page_to)]
            else:
                graph[page_from].append((len(page_names[page_to]), page_to))

            if graph.get(page_to) is None:
                graph[page_to] = []

    path = djikstra(graph, id_analytics, id_algorithm)
    path_str = ''
    for el in path:
        path_str += page_names[el]

    print(len(path_str))  # Длина кратчайшего пути, задача 3
    print(page_names.get(path[-2]))  # Название страницы, ссылающейся на Algorithms, задача 4
