# Task 1
## python -m doctest -v -o NORMALIZE_WHITESPACE main.py:
Происходит корректный запуск теста, проблем не возникает
## python -m doctest -v main.py:
Происходит 1 ошибка из-за лишнего пробела, тест проваливается
# Task 2
## python -m pytest main.py
Один провал 2 успеха. Провал из-за отсутствия в декодере пробелов между словами
# Task 3
## python -m unittest -v fit.py
Тесты пройдены успешно
# Task 4
## python -m pytest -v py_fit.py
Тесты пройдены успешно
# Task 5
## coverage run -m pytest -v Tic-Tac.py
Запуск тестирования
## coverage html
Создание директории html
##  htmlcov\index.html
Переход на нее
