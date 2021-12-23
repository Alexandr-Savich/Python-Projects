import click
from random import randint


class DictMixin:
    def dict(self):
        """Метод, реализуемый всеми тремя классами"""
        print(f'- {self.name}: {", ".join(self.recipe[self.name])}')


class Margherita(DictMixin):
    def __init__(self, size: str):
        self.name = 'Margherita'
        self.recipe = {self.name: ['tomato sauce', 'mozzarella', 'tomatoes']}
        if size == 'l':
            self.price = 5
        else:
            self.price = 7


class Pepperoni(DictMixin):
    def __init__(self, size: str):
        self.name = 'Pepperoni'
        self.recipe = {self.name: ['tomato sauce', 'mozzarella', 'pepperoni']}
        if size == 'l':
            self.price = 3
        else:
            self.price = 5


class Hawaiian(DictMixin):
    def __init__(self, size: str):
        self.name = 'Hawaiian'
        self.recipe = {self.name: ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']}
        if size == 'l':
            self.price = 1
        else:
            self.price = 3


@click.group()
def cli():
    pass


@cli.command()
def menu():
    """Выводит меню"""
    pizzas = [Margherita('L'), Pepperoni('L'), Hawaiian('L')]
    for pizza in pizzas:
        pizza.dict()


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.argument('size', nargs=1)
def order(pizza: str, size: str, delivery: bool):
    """Делает заказ и доставку по требованию"""
    bake(pizza, size)
    if delivery:
        deliver(pizza)


def bake(pizza: str, size: str):
    """Готовит пиццу и выводит стоимость заказа"""
    size = size.lower()
    pizza = pizza.lower()
    d = {'margherita': Margherita,
         'pepperoni': Pepperoni,
         'hawaiian': Hawaiian}
    if size not in ['l', 'xl'] or pizza not in d.keys():
        print('Incorrect size\n')
    else:
        print(f' Price = {d[pizza](size).price},\n Cooking...')


def timed_delivery(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(f' Delivery took {randint(15, 60)} minutes')
    return wrapper


@timed_delivery
def deliver(pizza: str):
    pass


if __name__ == '__main__':
    cli()
   
