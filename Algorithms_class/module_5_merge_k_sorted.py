from heapq import heapify, heapreplace, heappop


def merge_k_sorted(arrs: list) -> list:  # O(n)
    """
    Делает слияние нескольких отсортированных массивов в один.

    :param arrs: массивы, которые нужно соединить,
    :return: отсортированный массив.
    """
    res = []
    heap = [(arr[0], arr, 1) for arr in arrs if len(arr) > 0]

    heapify(heap)

    while len(heap):
        if len(heap) == 1:
            ind = heap[0][-1] - 1
            res += heap[0][1][ind:]
            break

        while True:
            value, arr, ind = heap[0]
            res.append(value)
            if ind == len(arr):
                heappop(heap)
                break
            else:
                heapreplace(heap, (arr[ind], arr, ind + 1))

    return res


def solution():
    arrs = read_multiline_input()  # эта функция уже написана
    merged = merge_k_sorted(arrs)
    print(' '.join([str(el) for el in merged]))


if __name__ == '__main__':
    solution()
