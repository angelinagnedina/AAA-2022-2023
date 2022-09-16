from typing import List

# Task 1
# вывести все элементы a, которые есть в b


def intersection_of_two_arrays(arr_1: List[int], arr_2: List[int]) -> List[int]:
    arr_2 = set(arr_2)
    return [el for el in arr_1 if el in arr_2]


print('Task 1:', intersection_of_two_arrays([0, 1, 2, 3, 4, 5, 6],  [3, 4, 5]))

# Task 2
# создайте новый массив с уникальными значениями


def unique_values(arr: List[int]) -> (List[int], List[int]):
    # Без сохранения порядка
    new_array_1 = list(set(arr))

    # С сохранением
    extra = set()
    new_array_2 = []
    for el in arr:
        if el not in extra:
            new_array_2.append(el)
            extra.add(el)

    return new_array_1, new_array_2


print('Task 2:', unique_values([0, 0, 1, 1, 2, 2]))

# Task 3
# создайте новый массив с четными элементами


def even_elements_of_array(arr: List[int]) -> List[int]:
    return [el for el in arr if el % 2 == 0]


print('Task 3:', even_elements_of_array([0, 1, 2, 3, 4, 5]))

# Task 4
# создайте словарь из списка, где ключ - индекс этого элемента


def make_dict_from_array(arr: list) -> dict:
    return dict((ind, value) for ind, value in enumerate(arr))


print('Task 4:', make_dict_from_array(['foo', 'bar', 'baz']))

# Task 5
# распечатайте приветствия


def greetings(arr: List[str]) -> None:
    for name in arr:
        print('F-strings: ' + f'Hi, {name}!')
        print('Format: ' + 'Hi, {}!'.format(name))
        print('S: ' + 'Hi, %s!' % name)


print('Task 5:')
greetings(['John', 'Allison', 'Brian', 'Claire', 'Andrew'])

# Task 6:
# напечатайте все элементы из a, которые отсутствуют в b


def difference(arr_1: list, arr_2: list) -> list:
    arr_2 = set(arr_2)
    return [el for el in arr_1 if el not in arr_2]


print('Task 6: отсутствуют', difference(['foo', 'bar', 'baz', 'egg'], ['bar', 'baz']))


# Task 7
# склейте 2 массива. результат - отсортированный массив


def unite_two_arrays(arr_1: List[int], arr_2: List[int]) -> (List[int], List[int]):
    # First option (initial arrays are not sorted)
    new_arr_1 = sorted(arr_1 + arr_2)

    # Second option (initial arrays are sorted)
    new_arr_2 = []
    ind_1, ind_2 = 0, 0

    while ind_1 < len(arr_1) and ind_2 < len(arr_2):
        if arr_1[ind_1] <= arr_2[ind_2]:
            new_arr_2.append(arr_1[ind_1])
            ind_1 += 1
        else:
            new_arr_2.append(arr_2[ind_2])
            ind_2 += 1

    if ind_1 < len(arr_1):
        for el in arr_1[ind_1:]:
            new_arr_2.append(el)
    if ind_2 < len(arr_2):
        for el in arr_2[ind_2:]:
            new_arr_2.append(el)

    return new_arr_1, new_arr_2


print('Task 7:', unite_two_arrays([0, 1, 2, 6, 7, 8], [3, 4, 5]))

# Task 8
# создайте новый словарь из a с отсортированными ключами в обратном порядке


def reverse_keys(d: dict) -> dict:
    return dict(zip(reversed(d.keys()), d.values()))


print('Task 8:', reverse_keys({0: 'foo', 1: 'bar', 2: 'baz'}))
