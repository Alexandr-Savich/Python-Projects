import urllib.request
import json
from unittest.mock import patch
import pytest

API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год
    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']
    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str)


def test_raise_exception():
    data = {'currentDateTime': '1999,12,22'}

    with open('exception_test.json', 'w+') as exc_test:
        json.dump(data, exc_test)
        exc_test.seek(0)
        with pytest.raises(ValueError):
            with patch.object(urllib.request, 'urlopen', return_value=exc_test):
                result = what_is_year_now()


def test_year():
    dates = [({'currentDateTime': '22.12.1999'}, 1999),({'currentDateTime': '2018-09-01'}, 2018)]
    for date in dates:
        with open('date_test.json', 'w+') as test:
            json.dump(date[0], test)
            test.seek(0)
            with patch.object(urllib.request, 'urlopen', return_value=test):
                func_year = what_is_year_now()

        assert func_year == date[1], f'Expected {date[1]}, got {func_year}'
