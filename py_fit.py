from typing import List, Tuple
import pytest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


@pytest.mark.parametrize('vector,expected', [
    (['Moscow', 'New York', 'Moscow', 'London'],
     [('Moscow', [0, 0, 1]),
      ('New York', [0, 1, 0]),
      ('Moscow', [0, 0, 1]),
      ('London', [1, 0, 0])]),
    (['one', 'hot', 'encoding', 'rules'],
     [('one', [0, 0, 0, 1]),
      ('hot', [0, 0, 1, 0]),
      ('encoding', [0, 1, 0, 0]),
      ('rules', [1, 0, 0, 0])])
])
def test_fit_transform(vector, expected):
    assert fit_transform(vector) == expected, f'Expected{expected}, got{fit_transform(vector)}'


def test_argless():
    with pytest.raises(TypeError):
        exception = fit_transform()


def test_single():
    assert fit_transform('ABC') != [], f'Failed on 1 item'


def test_empty():
    assert fit_transform([]) == [], f'Failed on empty array'


if __name__ == '__main__':
    pass
