import pizza_project as pp
from click.testing import CliRunner
from unittest.mock import patch
from io import StringIO
import sys


def test1_pizza():
    pizza1 = pp.Margherita('L')
    pizza2 = pp.Pepperoni('L')
    assert pizza1 != pizza2


def test2_pizza():
    pizza1 = pp.Hawaiian('L')
    pizza2 = pp.Hawaiian('L')
    assert pizza1 == pizza2


def test3_pizza():
    pizza = pp.Margherita('S')
    ingredients = pizza.dict()
    assert ('mozzarella', '300g') in ingredients.items()


def test_log():
    pattern = 'Какой-то шаблон {}'
    wrapper = pp.log(pattern)(lambda x: True)
    captured_output = StringIO()
    sys.stdout = captured_output
    with patch('pizza_project.time_ns', return_value=1):
        res = wrapper(0)
        sys.stdout = sys.__stdout__
        assert captured_output.getvalue() == 'Какой-то шаблон 0\n'
        assert res


def test_deliver():
    assert pp.deliver()


def test_cook():
    dish1 = pp.cook('margherita', 'M')
    dish2 = pp.cook('pepperoni', 'S')
    dish3 = pp.cook('hawaiian', 'L')
    dish4 = pp.cook('hotdog', 'M')

    assert dish1 == pp.Margherita('M')
    assert dish2 == pp.Pepperoni('S')
    assert dish3 == pp.Hawaiian('L')
    assert dish4 is None


def test1_order():
    result = CliRunner().invoke(pp.order, ['margherita', 'X'])
    assert result.output == 'Выберите другой размер.\n'


def test2_order():
    result = CliRunner().invoke(pp.order, ['margherita', 'L', '--delivery'])
    assert '‍🍳 Приготовили за' in result.output
    assert '🚗 Доставили за' in result.output


def test3_order():
    result = CliRunner().invoke(pp.order, ['hotdog', 'L', '--delivery'])
    assert result.output == 'Пожалуйста, выберите пиццу из меню.\n'


def test_menu():
    result = CliRunner().invoke(pp.cli, ['menu'])
    assert result.output == 'Margherita 🧀: tomato sauce, mozzarella, tomatoes\n' \
                            'Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n' \
                            'Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapples\n'
