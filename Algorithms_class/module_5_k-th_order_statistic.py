from heapq import heapify, heappop


def get_kth_element(arr: list, k: int) -> int:  # O(NlogN)
    """
    Ищет k-ый по порядку элемент массива.

    :param arr: изначальный массив,
    :param k: порядковая статистика,
    :return: число, соответствующее k-ой статистике.
    """
    heapify(arr)
    el = None

    for i in range(k + 1):
        el = heappop(arr)

    return el


def solution():
    arr = list(map(int, input().split()))
    k = int(input())
    print(get_kth_element(arr, k))


if __name__ == '__main__':
    solution()
