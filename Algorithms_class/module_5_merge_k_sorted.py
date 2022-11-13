from heapq import heapify, heapreplace, heappop


def merge_k_sorted(arrs: list) -> list:
    res = []
    heap = []

    for arr in arrs:
        if len(arr) > 0:
            heap.append([arr[0], arr, 1])

    heapify(heap)

    while len(heap) > 1:
        try:
            while True:
                value, arr, ind = heap[0]
                res.append(value)
                heapreplace(heap, [arr[ind], arr, ind + 1])
        except IndexError:
            heappop(heap)

    ind = heap[0][-1] - 1
    res += heap[0][1][ind:]

    return res


def solution():
    arrs = read_multiline_input()  # эта функция уже написана
    merged = merge_k_sorted(arrs)
    print(' '.join([str(el) for el in merged]))


if __name__ == '__main__':
    solution()
