from typing import List, Iterable


class CountVectorizer:
    """
    Convert a collection of text documents to a matrix of token counts.
    """

    def __init__(self):
        self.count_matrix = None
        self.data = {}

    def fit_transform(self, text: Iterable[str]) -> List[List[int]]:
        """
        Для данной на вход коллекции слов подсчитывает число вхождения уникальных слов для каждой
        строки коллекции и возвращает соответствующую матрицу.

        :param text: коллекция из строк,
        :return: матрица, где строка соответствует строке из коллекции, и для неё подсчитано число
            вхождений слов из коллекции уникальных слов.
        """
        dim = len(text)
        for ind, string in enumerate(text):
            words = string.lower().split()
            for word in words:
                if not self.data.get(word):
                    self.data[word] = [0 for _ in range(dim)]
                    self.data[word][ind] = 1
                else:
                    self.data[word][ind] += 1

        matrix = [[0 for _ in range(len(self.data))] for _ in range(dim)]
        for i in range(dim):
            for ind, value in enumerate(self.data.values()):
                matrix[i][ind] = value[i]

        self.count_matrix = matrix

        return self.count_matrix

    def get_feature_names(self) -> List[str]:
        """
        Возвращает уникальные слова, встретившиеся в тексте.

        :return: список, состоящий из уникальных слов.
        """
        return list(self.data.keys())


def test(ground_truth: tuple, result: tuple) -> None:
    """
    Кривое сравнение результатов истинных результатов с тем, что выдаёт мой CountVectorizer.
    За истинные результаты считаю выдачу sklearn.feature_extraction.text.CountVectorizer.
    Для каждого уникального слова выводит список, где на i-ой позиции стоит True, если
    это слово вошло в i-ый элемент коллекции равное число раз для sklearn и моей реализации.

    :param ground_truth: кортеж с результатами от sklearn, где первый элемент - список из
        уникальных слов в некоторой коллекции, второй элемент - матрица.
    :param result: то же самое, только результаты моей реализации CountVectorizer.
    """
    true_feature_names = ground_truth[0]
    num_strings = len(ground_truth[1])
    extra_array = [False for _ in range(num_strings)]

    for ind, word in enumerate(true_feature_names):
        print(f'{word}: ', end='')
        try:
            ind_in_result = result[0].index(word)
            for i in range(num_strings):
                extra_array[i] = result[1][i][ind_in_result] == ground_truth[1][i][ind]
            print(extra_array)
        except ValueError:
            print('Значение не найдено в моей реализации')
            break


if __name__ == '__main__':
    tests = [['Crock Pot Pasta Never boil pasta again',
              'Pasta Pomodoro Fresh ingredients Parmesan to taste'],
             ['This is the first document',
              'This document is the second document',
              'And this is the third one',
              'Is this the first document'],
             ['Не уходи смиренно в сумрак вечной тьмы',
              'Пусть тлеет бесконечность в яростном закате',
              'Пылает гнев на то как гаснет смертный мир',
              'Пусть мудрецы твердят что прав лишь тьмы покой',
              'И не разжечь уж тлеющий костёр',
              'Не уходи смиренно в сумрак вечной тьмы',
              'Пылает гнев на то как гаснет смертный мир',
              'Не гасни уходя во мрак ночной']
             ]

    ground_truth = [(['again', 'boil', 'crock', 'fresh', 'ingredients', 'never',  # First test
                      'parmesan', 'pasta', 'pomodoro', 'pot', 'taste', 'to'],
                     [[1, 1, 1, 0, 0, 1, 0, 2, 0, 1, 0, 0],
                      [0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1]]),
                    (['and', 'document', 'first', 'is', 'one', 'second', 'the',  # Second test
                      'third', 'this'],
                     [[0, 1, 1, 1, 0, 0, 1, 0, 1],
                      [0, 2, 0, 1, 0, 1, 1, 0, 1],
                      [1, 0, 0, 1, 1, 0, 1, 1, 1],
                      [0, 1, 1, 1, 0, 0, 1, 0, 1]]),
                    (['бесконечность', 'вечной', 'во', 'гаснет', 'гасни', 'гнев',  # Third test
                      'закате', 'как', 'костёр', 'лишь', 'мир', 'мрак', 'мудрецы',
                      'на', 'не', 'ночной', 'покой', 'прав', 'пусть', 'пылает', 'разжечь',
                      'смертный', 'смиренно', 'сумрак', 'твердят', 'тлеет', 'тлеющий',
                      'то', 'тьмы', 'уж', 'уходи', 'уходя', 'что', 'яростном'],
                     [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
                       1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                      [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
                       0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                      [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1,
                       0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0,
                       0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0,
                       0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
                      [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
                       1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
                      [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1,
                       0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0,
                       0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]])]

    for num in range(len(tests)):
        print(f'Тест {num + 1}')
        vectorizer = CountVectorizer()
        count_matrix = vectorizer.fit_transform(tests[num])
        result = (vectorizer.get_feature_names(), count_matrix)
        test(ground_truth[num], result)
        print()

