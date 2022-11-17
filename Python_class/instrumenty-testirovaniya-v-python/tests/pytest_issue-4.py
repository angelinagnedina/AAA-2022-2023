from one_hot_encoder import fit_transform
import pytest


def test_1():
    colors = ['red', 'blue', 'yellow', 'blue']
    res = [
        ('red', [0, 0, 1]),
        ('blue', [0, 1, 0]),
        ('yellow', [1, 0, 0]),
        ('blue', [0, 1, 0])
    ]
    assert fit_transform(colors) == res


def test_2():
    coffee = ['raf', 'cappuccino', 'filter', 'filter', 'latte']
    res = [
        ('raf', [0, 0, 0, 1]),
        ('cappuccino', [0, 0, 1, 0]),
        ('filter', [0, 1, 0, 0]),
        ('filter', [0, 1, 0, 0]),
        ('latte', [1, 0, 0, 0])
    ]
    assert fit_transform(coffee) == res


def test_3():  # С перехватом исключения
    poets = ['Brodskiy', 'Lermontov']
    res = [
        ('Brodskiy', [1, 0]),
        ('Lermontov', [1, 0])
    ]
    with pytest.raises(AssertionError):
        assert fit_transform(poets) == res


def test_4():
    poets = ['Brodskiy', 'Lermontov', 'Dostoevsky']
    res = ('Brodskiy', [0, 0, 1])
    assert res in fit_transform(poets)
