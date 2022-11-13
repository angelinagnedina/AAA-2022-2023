import unittest
from one_hot_encoder import fit_transform


class TestFitTransform(unittest.TestCase):
    def test_1(self):
        colors = ['red', 'blue', 'yellow', 'blue']
        res = [
            ('red', [0, 0, 1]),
            ('blue', [0, 1, 0]),
            ('yellow', [1, 0, 0]),
            ('blue', [0, 1, 0])
        ]
        self.assertEqual(fit_transform(colors), res)

    def test_2(self):
        coffee = ['raf', 'cappuccino', 'filter', 'filter', 'latte']
        res = [
            ('raf', [0, 0, 0, 1]),
            ('filter', [0, 1, 0, 0]),
            ('filter', [0, 1, 0, 0]),
            ('cappuccino', [0, 0, 1, 0]),
            ('latte', [1, 0, 0, 0])
        ]
        self.assertCountEqual(fit_transform(coffee), res)

    def test_3(self):  # Пример с перехватом исключения
        poets = ['Brodskiy', 'Lermontov']
        res = [
            ('Brodskiy', [1, 0]),
            ('Lermontov', [1, 0])
        ]
        try:
            self.assertEqual(output := fit_transform(poets), res)
        except AssertionError:
            print(f'\n\033[1;38;2;255;0;0mAssertionError in test_3'
                  f': expected: {res}, got: {output}\033[0m')

    def test_4(self):
        poets = ['Brodskiy', 'Lermontov']
        res = ('Brodskiy', [0, 1])
        self.assertTupleEqual(res, fit_transform(poets)[0])


if __name__ == '__main__':
    unittest.main()
