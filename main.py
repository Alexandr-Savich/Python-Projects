
import random
import abc
import json


class AnimeMon(abc.ABC):
    @abc.abstractmethod
    def inc_exp(self, value: int):
        raise IndexError


class BasePokemon:
    def __str__(self):
        return f'{self.name}/{self.poketype}'


class EmodjiMixin:
    emodji = {
        'grass': '🌿',
        'fire': '🔥',
        'water': '🌊',
        'electric': '⚡',
    }

    def __str__(self):
        text_pocketype = super().__str__()
        return text_pocketype.replace(self.poketype, self.emodji[self.poketype])


class Pokemon(EmodjiMixin, BasePokemon, AnimeMon):
    def __init__(self, name: str, poketype: str):
        self.name = name
        self.poketype = poketype
        self.exp = 0

    def inc_exp(self, exp: int):
        self.exp += exp


def train(mon: AnimeMon):
    step_size, level_size = 10, 100
    sparring_qty = (level_size - mon.exp % level_size) // step_size
    for i in range(sparring_qty):
        win = random.choice([True, False])
        if win:
            mon.inc_exp(step_size)


class Digimon(AnimeMon):
    def __init__(self, name: str):
        self.name = name
        self.exp = 0

    def inc_exp(self, value: int):
        self.exp += value * 8


class ColorizeMixin:
    def color_print(self, text: str, repr_color_code: int):
        return f'\033[{repr_color_code}m{text}'


class Advert(ColorizeMixin):
    repr_color_code = 33

    @property
    def price(self):
        if '_Advert__price' in self.__dict__:
            return self.__price
        else:
            return 0

    def __transform(self, d: dict):
        for key, value in d.items():

            if isinstance(value, dict):
                self.__dict__[key] = Advert(value)
            else:
                if key == 'price':
                    if value < 0:
                        print('Price must be >0')
                        raise ValueError
                    else:
                        self.__price = value
                    continue
                self.__dict__[key] = value

    def __init__(self, ad: dict):
        self.__transform(ad)

    def __repr__(self):
        return self.color_print(f'{self.title} | {self.price} ₽', self.repr_color_code)


if __name__ == '__main__':
    pikachu = Pokemon(name='Pikachu', poketype='electric')
    train(pikachu)
    print(f'Pikachu:{pikachu.exp}')
    agumon = Digimon(name='Agumon')
    train(agumon)
    print(f'Agumon:{agumon.exp}')

    lesson_str = """{
    "title": "python",
    "price": 2128506,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
    }"""
    lesson = json.loads(lesson_str)
    print(lesson)

    ad = Advert(lesson)
    print(ad)
