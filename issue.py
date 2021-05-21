import json
from keyword import iskeyword


class ColorizeMixin:
    def __repr__(self) -> str:
        return f"\033[1;{self.repr_color_code};40m{self.title} | {self.price} ₽"


class JsonConverter:
    def __init__(self, obj: dict):
        for k, v in obj.items():
            if iskeyword(k):
                k += "_"
            if isinstance(v, dict):
                setattr(self, k, JsonConverter(v))
            else:
                setattr(self, k, v)


class Advert(ColorizeMixin, JsonConverter):
    repr_color_code = 33

    def __repr__(self) -> str:
        res = super().__repr__()
        return res

    def __init__(self, obj: dict):
        super().__init__(obj)

        if not hasattr(self, "title"):
            raise KeyError("Отсутствует поле title")
        if not hasattr(self, 'price'):
            self.price = 0

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price: int):
        if price < 0:
            raise ValueError('price must be >=0')
        self._price = price


if __name__ == '__main__':
    data = """{
        "title": "python",
        "price": 0,
        "location": {
            "address": "город Москва, Лесная, 7",
            "metro_stations": ["Белорусская"]
            }
        }"""
    data_c = """{
        "title": "Вельш-корги",
        "price": 1000,
        "class": "dogs",
        "location": {
            "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
            }
        }"""

    advert = Advert(json.loads(data))
    corgi = Advert(json.loads(data_c))
    print(advert.price)
    print(advert.location.address)
    print(corgi.class_)
    print(corgi)
