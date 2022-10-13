from typing import List, Iterable
from math import log


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


class TfidfTransformer:
    """
        Computes Tf-Idf matrix given count_matrix of a corpus.
    """
    def tf_transform(self, count_matrix) -> List[List[float]]:
        """
        :param count_matrix: matrix of size (num_doc, num_unique_words), where in each row
         stored the number of times some unique word appears in a corresponding document.
        :return: matrix of size (num_doc, num_unique_words), where in each row stored
         frequencies of each unique word in corresponding document.
        """
        tf_matrix = []

        for line in count_matrix:
            sum_of_el = sum(line)
            new_line = []
            for el in line:
                new_line.append(round(el / sum_of_el, 3))
            tf_matrix.append(new_line)

        return tf_matrix

    def idf_transform(self, count_matrix: List[List[int]]) -> List[float]:
        """
        :param count_matrix: matrix of size (num_doc, num_unique_words), where in each row
         stored the number of times some unique word appears in a corresponding document.
        :return: vector of size len(unique_words), storing how rarely each unique word appears
         in all documents (exapmle: a word that appears in each document will have 0 in a
          corresponding place in the vector).
        """
        num_of_doc = len(count_matrix)
        num_of_unique_words = len(count_matrix[0]) if num_of_doc else 0
        idf_matrix = []

        for i in range(num_of_unique_words):
            frec_of_word = 0

            for j in range(num_of_doc):
                frec_of_word += bool(count_matrix[j][i])

            res = log((num_of_doc + 1) / (frec_of_word + 1)) + 1
            idf_matrix.append(round(res, 3))

        return idf_matrix

    def fit_transform(self, count_matrix) -> List[List[float]]:
        """
        :param count_matrix: matrix of size (num_doc, num_unique_words), where in each row
         stored the number of times some unique word appears in a corresponding document.
        :return: Tf-Idf matrix.
        """
        tf_matrix = self.tf_transform(count_matrix)
        idf_matrix = self.idf_transform(count_matrix)
        tfidf = []

        for row in tf_matrix:
            tfidf.append([round(tf * idf, 3) for tf, idf in zip(row, idf_matrix)])

        return tfidf


class TfidfVectorizer(CountVectorizer):
    """
        Computes Tf-Idf matrix for a given corpus of documents.
    """
    def __init__(self):
        super().__init__()
        self.transformer = TfidfTransformer()

    def fit_transform(self, corpus) -> List[List[float]]:
        count_matrix = super().fit_transform(corpus)
        return self.transformer.fit_transform(count_matrix)


if __name__ == '__main__':
    corpus = ['Crock Pot Pasta Never boil pasta again',
              'Pasta Pomodoro Fresh ingredients Parmesan to taste']

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names()
