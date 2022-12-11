import click
from time import time_ns
from typing import Any


class Pizza:
    """Класс, который содержит базовую информацию о пицце."""
    SIZES = {
        'S': 1,
        'M': 2,
        'L': 3,
        'XL': 4
    }

    def __init__(self, pizza_name: str = '', size: str = '', icon: str = ''):
        self.pizza_name = pizza_name.lower()
        self.size = size
        self.ingredients: list = []
        self.icon = icon
        # Кол-во ингредиентов сделаем зависимым от размера
        self.multiplier = self.SIZES[size]

    def dict(self) -> dict:
        """Возвращает ингредиенты для пиццы в виде словаря."""
        ingredients_dict = {}

        for ingredient, amount, count in self.ingredients:
            ingredients_dict[ingredient] = f'{self.multiplier * amount}{count}'

        return ingredients_dict

    def __eq__(self, other) -> bool:
        """Сравнивает две пиццы."""
        # Удостоверимся, что сравниваем пиццу с пиццей.
        assert isinstance(other, Pizza), f'{other} is not a pizza!'
        return self.pizza_name == other.pizza_name and self.size == other.size


class Margherita(Pizza):
    def __init__(self, size: str = 'S'):
        super().__init__('margherita', size, '🧀')
        self.ingredients = [
            ('tomato sauce', 100, 'ml'),
            ('mozzarella', 300, 'g'),
            ('tomatoes', 2, '')
        ]


class Pepperoni(Pizza):
    def __init__(self, size: str = 'S'):
        super().__init__('pepperoni', size, '🍕')
        self.ingredients = [
            ('tomato sauce', 80, 'ml'),
            ('mozzarella', 100, 'g'),
            ('pepperoni', 150, 'g')
        ]


class Hawaiian(Pizza):
    def __init__(self, size: str = 'S'):
        super().__init__('hawaiian', size, '🍍')
        self.ingredients = [
            ('tomato sauce', 60, 'ml'),
            ('mozzarella', 200, 'g'),
            ('chicken', 200, 'g'),
            ('pineapples', 100, 'g')
        ]


def log(pattern: str):
    """Декоратор, принимающий шаблон, в который подставляется время."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            time_start = time_ns()
            res = func(*args, **kwargs)
            # Если заказали пиццу не из меню - время готовки не выводим
            if res:
                time_end = time_ns()
                print(pattern.format(time_end - time_start))
            return res
        return wrapper
    return decorator


@log('🚗 Доставили за {} c.')
def deliver() -> bool:
    return True


@log('‍🍳 Приготовили за {} с.')
def cook(pizza: str, size: str = '') -> Any:
    pizza = pizza.lower()
    dish: Any = None

    if pizza == 'margherita':
        dish = Margherita(size)
    elif pizza == 'pepperoni':
        dish = Pepperoni(size)
    elif pizza == 'hawaiian':
        dish = Hawaiian(size)

    return dish


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.argument('size', nargs=1, default='S')
def order(pizza: str, size: str, delivery: bool):
    """Готовит и доставляет пиццу."""
    # Если размер пиццы не корректный - сообщаем об этом.
    if size not in Pizza.SIZES:
        print('Выберите другой размер.')
    else:
        dish = cook(pizza, size)

        # Если пиццы не оказалось в меню - сообщаем об этом.
        if dish is None:
            print('Пожалуйста, выберите пиццу из меню.')
        elif delivery:
            deliver()


@cli.command()
def menu():
    """Выводит меню."""
    pizzas = [Margherita(), Pepperoni(), Hawaiian()]
    for pizza in pizzas:
        products = ', '.join(pizza.dict().keys())
        click.echo(f'{pizza.pizza_name.capitalize()} {pizza.icon}: {products}')


if __name__ == '__main__':
    cli()
