import json
import keyword


class JsonToObject:
    """
        Class that transforms json-object to nested python objects.
    """
    def __init__(self, data: dict):
        for key, value in data.items():
            # Check whether key is the keyword in python,
            # if so - add '_' to key.
            if keyword.iskeyword(key):
                key += '_'

            # If value is dictionary - make another object.
            if isinstance(value, dict):
                new_obj = JsonToObject(value)
                setattr(self, key, new_obj)
            else:
                setattr(self, key, value)

    def __repr__(self):
        """
            In case we have nested dictionaries - they will be represented
            as instances of JsonToObject with collections of their keys.
        """
        keys = list(self.__dict__.keys())
        return f'<Instance of JsonToObject class with attributes: {", ".join(keys)}.>'


class ColorizeMixin:
    """
        Mixin class that changes the color of output in console.
    """
    def __str__(self):
        text = repr(self)
        color = getattr(self, 'repr_color_code', 35)
        return f'\033[{str(color)}m{text}'


class Advert(ColorizeMixin, JsonToObject):
    """
        Class that contains info about an item for advertisement.
    """
    repr_color_code = 34

    def __init__(self, data: dict):
        super().__init__(data)
        # Set price to 0 in case it wasn't mentioned.
        self.price = getattr(self, 'price', 0)
        assert self.price >= 0, 'Price must be non-negative!'

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


if __name__ == '__main__':
    corgi_str = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
        }
    }"""

    corgi = json.loads(corgi_str)
    corgi_ad = Advert(corgi)
    assert corgi_ad.location.address == "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
    print(corgi_ad)
