from pizza_project import Pizza, deliver, cook, order, cli, log
from click.testing import CliRunner
from unittest.mock import patch
from io import StringIO
import sys


def test1_pizza():
    pizza1 = Pizza('margherita', 'L')
    pizza2 = Pizza('margherita', 'XL')
    assert pizza1 != pizza2


def test2_pizza():
    pizza1 = Pizza('margherita', 'L')
    pizza2 = Pizza('margherita', 'L')
    assert pizza1 == pizza2


def test3_pizza():
    pizza = Pizza('margherita', 'L')
    captured_output = StringIO()
    sys.stdout = captured_output
    with patch.dict('pizza_project.RECIPE', {'margherita': [('tomato sauce', 50, 'ml')]}):
        pizza.dict()
        sys.stdout = sys.__stdout__
        assert captured_output.getvalue() == \
               'Рецепт для margherita размера L\ntomato sauce: 50ml\n'


def test_log():
    pattern = 'Какой-то шаблон {}'
    wrapper = log(pattern)(lambda x: True)
    captured_output = StringIO()
    sys.stdout = captured_output
    with patch('pizza_project.time_ns', return_value=1):
        res = wrapper(0)
        sys.stdout = sys.__stdout__
        assert captured_output.getvalue() == 'Какой-то шаблон 0\n'
        assert res


def test_deliver():
    dish1 = Pizza('margherita', 'L')
    dish2 = None
    assert deliver(dish1)
    assert not deliver(dish2)


def test1_cook():
    captured_output = StringIO()
    sys.stdout = captured_output
    res = cook('hotdog', 'L')
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == 'Пожалуйста, выберите пиццу из меню.\n'
    assert res is None


def test2_cook():
    captured_output = StringIO()
    sys.stdout = captured_output
    res = cook('margherita', 'X')
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue() == 'Пожалуйста, выберите другой размер.\n'
    assert res is None


def test3_cook():
    res = cook('margherita', 'L')
    assert res == Pizza('margherita', 'L')


def test1_order():
    result = CliRunner().invoke(order, ['margherita', 'X'])
    assert result.output == 'Пожалуйста, выберите другой размер.\n'


def test2_order():
    result = CliRunner().invoke(order, ['margherita', 'L', '--delivery'])
    assert '‍🍳 Приготовили за' in result.output
    assert '🚗 Доставили за' in result.output


def test_menu():
    result = CliRunner().invoke(cli, ['menu'])
    assert result.output == 'Margherita 🧀: tomato sauce, mozzarella, tomatoes\n' \
                            'Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n' \
                            'Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples\n'
