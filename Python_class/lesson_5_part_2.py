emoji = {
    'grass': '☘️',
    'fire': '🔥',
    'water': '💧',
    'electric': '⚡️'
}


class EmojiMixin:
    """
        Mixin that changes the output in the console in case it contains
        some keywords.
    """
    def __str__(self):
        text = f'{self.name}/{self.poketype}'
        for key, value in emoji.items():
            text = text.replace(key, value)
        return text


class Pokemon(EmojiMixin):
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype

    def __repr__(self):
        return f'{self.name}/{self.poketype}'


if __name__ == '__main__':
    bulbasaur = Pokemon(name='Bulbasaur', poketype='electric')
    print(bulbasaur)
