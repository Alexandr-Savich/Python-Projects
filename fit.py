from typing import List, Tuple
import unittest


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


class Test_fit(unittest.TestCase):

    def test_encoding(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]

        words = ['one', 'hot', 'encoding', 'rules']
        exp_transformed_words = [
            ('one', [0, 0, 0, 1]),
            ('hot', [0, 0, 1, 0]),
            ('encoding', [0, 1, 0, 0]),
            ('rules', [1, 0, 0, 0])
        ]
        self.assertEqual(fit_transform(cities), exp_transformed_cities, 'City transformation failed')
        self.assertEqual(fit_transform(words), exp_transformed_words, 'Words transformation failed')

    def test_argless(self):
        with self.assertRaises(TypeError):
            exception = fit_transform()

    def test_single(self):
        self.assertNotEqual(fit_transform('ABC'), [])

    def test_empty(self):
        self.assertEqual(fit_transform([]), [])


if __name__ == '__main__':
    print(fit_transform([]))
