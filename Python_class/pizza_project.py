class Pizza:
    def __init__(self, pizza_name: str = None, size: str = None):
        # Проверка, что данная пицца данного размера есть в меню
        if pizza_name.lower() not in ['margherita', 'pepperoni', 'hawaiian']:
            print('There is no such pizza in the menu :(')
        elif size not in ['L', 'XL']:
            print('Please choose different size')
        else:
            self.pizza_name = pizza_name.lower()
            self.size = size
            # Кол-во ингредиентов сделаем зависимым от размера
            multiplier = 1 if self.size == 'L' else 2

            if self.pizza_name == 'margherita':
                self.ingredients = dict([
                    ('tomato sauce', f'{multiplier * 100} ml'),
                    ('mozzarella', f'{multiplier * 300} g'),
                    ('tomatoes', f'{multiplier * 2}')
                ])

            if self.pizza_name == 'pepperoni':
                self.ingredients = dict([
                    ('tomato sauce', f'{multiplier * 80} ml'),
                    ('mozzarella', f'{multiplier * 100} g'),
                    ('pepperoni', f'{multiplier * 150} g')
                ])

            if self.pizza_name == 'hawaiian':
                self.ingredients = dict([
                    ('tomato sauce', f'{multiplier * 60} ml'),
                    ('mozzarella', f'{multiplier * 200} g'),
                    ('chicken', f'{multiplier * 200} g'),
                    ('pineapples', f'{multiplier * 100} g')
                ])

    def dict(self):
        print(f'Recipe for {self.pizza_name} of size {self.size}')

        for ingredient, amount in self.ingredients.items():
            print(f'{ingredient}: {amount}')

    def __eq__(self, other):
        # Удостоверимся, что сравниваем пиццу с пиццей
        assert isinstance(other, Pizza), f'{other} is not a pizza!'

        # Проверим, что пиццы и размеры идентичны
        for ingredient, amount in other.ingredients.items():
            amount_2 = self.ingredients.get(ingredient)
            if amount_2 is None or amount_2 != amount:
                return False

        for ingredient, amount in self.ingredients.items():
            amount_2 = other.ingredients.get(ingredient)
            if amount_2 is None or amount_2 != amount:
                return False

        return True


if __name__ == '__main__':
    hav = Pizza('Hawaiian', 'L')
    hav2 = Pizza('Hawaiian', 'L')
    print(hav == hav2)
