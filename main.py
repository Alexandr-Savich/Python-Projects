import csv
from collections import defaultdict


def print_dict(d, indent=0) -> None:
    """Печатает словарь в читабельном виде"""
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            print_dict(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(value))


def read_file() -> list:
    """Читает таблицу из файла и возвращает лист из строк"""
    with open('Corp_Summary.csv', newline='', encoding="utf8") as file:
        reader = csv.DictReader(file, delimiter=';')
        data = []
        for i in reader:
            data.append(i)
    return data


def get_departments_structure(data: list) -> None:
    """Выполняет первый запрос (создает словарь из депортаментов разбитых на отделы с числом сотрудников в
    отделе) """
    departments = {}
    for row in data:
        key = row['Департамент']
        departments[key] = defaultdict(int)

    for row in data:
        key = row['Департамент']
        departments[key][row['Отдел']] += 1
    print_dict(departments)


def get_statistics(data: list) -> dict:
    """Выполняет второй запрос (создает словарь словарей из департаментов с ЗП и прочим)"""
    departments = {}
    for row in data:
        key = row['Департамент']
        departments[key] = defaultdict(float)

    for row in data:
        key = row['Департамент']
        departments[key]['Численность работников'] += 1

        if int(departments[key]['Минимальная зарплата']) == 0:
            departments[key]['Минимальная зарплата'] = float(row['Оклад'])
        if departments[key]['Минимальная зарплата'] > float(row['Оклад']):
            departments[key]['Минимальная зарплата'] = float(row['Оклад'])

        if departments[key]['Максимальная зарплата'] < float(row['Оклад']):
            departments[key]['Максимальная зарплата'] = float(row['Оклад'])

        departments[key]['Всего'] += float(row['Оклад'])

        departments[key]['Средняя зарплата'] = departments[key]['Всего'] / departments[key][
            'Численность работников']

    for i in departments.keys():
        departments[i].pop('Всего')
    return departments


def print_csv_dict(departments: dict):
    """Сохраняет departments.csv файл со статистикой по департаментам"""

    with open('departments.csv', 'w', newline='', encoding="utf8") as file:
        key = departments.keys()
        fieldnames = ['Департамент']
        fieldnames = fieldnames + (list(departments[list(key)[0]].keys()))

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for department in departments:
            d = {key: value for key, value in departments[department].items()}
            d['Департамент'] = department
            writer.writerow(d)

    print('Файл departments.csv успешно сохранён!\n')


def save_csv(departments: dict) -> dict:
    """Запускает печать в файл словаря"""
    print_csv_dict(departments)


def get_inquiry(data: list) -> None:
    """Получает запрос с клавиатуры"""

    menu = ''
    options = {'1': get_departments_structure,
               '2': get_statistics,
               '3': get_statistics}
    print('Выберите:{}/{}/{}'.format(*options))
    menu = input()
    while menu not in options:
        print('Выберите:{}/{}/{}'.format(*options))
        menu = input()
    dep = options[menu](data)
    if menu == '2':
        print_dict(dep)
    if menu == '3':
        save_csv(dep)


if __name__ == '__main__':
    data = read_file()
    get_inquiry(data)
