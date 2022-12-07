import click
from time import time_ns
from typing import Any


RECIPE = {
    'margherita': [
        ('tomato sauce', 100, 'ml'),
        ('mozzarella', 300, 'g'),
        ('tomatoes', 2, '')
    ],
    'pepperoni': [
        ('tomato sauce', 80, 'ml'),
        ('mozzarella', 100, 'g'),
        ('pepperoni', 150, 'g')
    ],
    'hawaiian': [
        ('tomato sauce', 60, 'ml'),
        ('mozzarella', 200, 'g'),
        ('chicken', 200, 'g'),
        ('pineapples', 100, 'g')
    ]
}


class Pizza:
    """Класс, который содержит информацию о пицце, доступной в меню."""
    def __init__(self, pizza_name: str, size: str):
        self.pizza_name = pizza_name.lower()
        self.size = size
        # Кол-во ингредиентов сделаем зависимым от размера
        self.multiplier = 1 if self.size == 'L' else 2

    def dict(self):
        """Выводит ингредиенты для пиццы."""
        print(f'Рецепт для {self.pizza_name} размера {self.size}')
        ingredients = RECIPE[self.pizza_name]

        for ingredient, amount, count in ingredients:
            print(f'{ingredient}: {self.multiplier * amount}{count}')

    def __eq__(self, other) -> bool:
        """Сравнивает две пиццы."""
        # Удостоверимся, что сравниваем пиццу с пиццей
        assert isinstance(other, Pizza), f'{other} is not a pizza!'
        return self.pizza_name == other.pizza_name and self.size == other.size


def log(pattern: str):
    """Декоратор, принимающий шаблон, в который подставляется время."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            time_start = time_ns()
            res = func(*args, **kwargs)
            # Если в процессе выполнения заказа произошла ошибка -
            # время не выводим
            if res:
                time_end = time_ns()
                print(pattern.format(time_end - time_start))
            return res
        return wrapper
    return decorator


@log('🚗 Доставили за {} c.')
def deliver(dish: Pizza) -> bool:
    # Отклоняем доставку, если заказ некорректный
    return True if dish else False


@log('‍🍳 Приготовили за {} с.')
def cook(pizza: str, size: str) -> Any:
    dish = None

    # Не готовим пиццу, если заказ не корректный
    if pizza.lower() not in RECIPE.keys():
        print('Пожалуйста, выберите пиццу из меню.')
    elif size not in ['L', 'XL']:
        print('Пожалуйста, выберите другой размер.')
    else:
        dish = Pizza(pizza, size)

    return dish


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.argument('size', nargs=1, default='L')
def order(pizza: str, size: str, delivery: bool):
    """Готовит и доставляет пиццу."""
    dish = cook(pizza, size)

    if delivery:
        deliver(dish)


@cli.command()
def menu():
    """Выводит меню."""
    icons = {
        'margherita': '🧀',
        'pepperoni': '🍕',
        'hawaiian': '🍍'
    }
    for pizza, ingredients in RECIPE.items():
        products = ', '.join([ingredient[0] for ingredient in ingredients])
        click.echo(f'{pizza.capitalize()} {icons[pizza]}: {products}')


if __name__ == '__main__':
    cli()
