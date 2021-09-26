if __name__ == '__main__':
    import csv


    def print_dict(d, indent=0) -> None:
        """Печатает словарь в читабельном виде"""
        for key, value in d.items():
            print('\t' * indent + str(key))
            if isinstance(value, dict):
                print_dict(value, indent + 1)
            else:
                print('\t' * (indent + 1) + str(value))


    def read_file():
        """Читает таблицу из файла, считает число строк и возвращает словарь из строк и их число"""
        with open('Corp_Summary.csv', newline='', encoding="utf8") as file:
            reader = csv.DictReader(file, delimiter=';')
            count = 0
            data = {}
            for i in reader:
                data[count] = i
                count = count + 1
        return data, count


    def action_1(data: dict, count: int) -> None:
        """Выполняет первый запрос (создает словарь из депортаментов разбитых на отделы с числом сотрудников в
        отделе) """
        departments = {}
        for i in range(count):
            key = data.get(i).get('Департамент')
            departments[key] = {}

        for i in range(count):
            key = data.get(i).get('Департамент')
            if departments.get(key).get(data.get(i).get('Отдел')) is None:
                departments.get(key)[data.get(i).get('Отдел')] = 1
            else:
                departments.get(key)[data.get(i).get('Отдел')] += 1
        print_dict(departments)


    def action_2(data: dict, count: int) -> dict:
        """Выполняет второй запрос (создает словарь словарей из департаментов с ЗП и прочим)"""
        departments = {}
        for i in range(count):
            key = data.get(i).get('Департамент')
            departments[key] = {}
        for i in range(count):
            key = data.get(i).get('Департамент')
            if departments.get(key).get('Численность работников') is None:
                departments.get(key)['Численность работников'] = 1
            else:
                departments.get(key)["Численность работников"] += 1

            if departments.get(key).get('Минимальная зарплата') is None:
                departments.get(key)['Минимальная зарплата'] = data.get(i).get('Оклад')
            else:
                if float(departments.get(key).get('Минимальная зарплата')) > float(data.get(i).get('Оклад')):
                    departments.get(key)['Минимальная зарплата'] = data.get(i).get('Оклад')

            if departments.get(key).get('Максимальная зарплата') is None:
                departments.get(key)['Максимальная зарплата'] = data.get(i).get('Оклад')
            else:
                if float(departments.get(key).get('Максимальная зарплата')) < float(data.get(i).get('Оклад')):
                    departments.get(key)['Максимальная зарплата'] = data.get(i).get('Оклад')

            if departments.get(key).get('Всего') is None:
                departments.get(key)['Всего'] = float(data.get(i).get('Оклад'))
            else:
                departments.get(key)['Всего'] += float(data.get(i).get('Оклад'))

            departments.get(key)['Средняя зарплата'] = departments.get(key)['Всего'] / departments.get(key)[
                'Численность работников']

        for i in departments.keys():
            departments.get(i).pop('Всего')
        return departments


    def print_csv_dict(departments: dict):
        """Сохраняет departments.csv файл со статистикой по департаментам"""

        with open('departments.csv', 'w', newline='', encoding="utf8") as file:
            fieldnames = ['Департамент', 'Численность работников', 'Максимальная зарплата', 'Минимальная зарплата',
                          'Средняя зарплата']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            for department in departments:
                writer.writerow({'Департамент': department,
                                 'Численность работников': departments[department]['Численность работников'],
                                 'Минимальная зарплата': departments[department]['Минимальная зарплата'],
                                 'Максимальная зарплата': departments[department]['Максимальная зарплата'],
                                 'Средняя зарплата': departments[department]['Средняя зарплата']})

        print('Файл departments.csv успешно сохранён!\n')


    def action_3(departments: dict) -> dict:
        """Запускает печать в файл словаря"""
        print_csv_dict(departments)


    def get_inquery(data: dict, count: int) -> None:
        """Получает запрос с клавиатуры и обрабатыает исключение"""
        try:
            j = int(input())
            if int(j) == 1:
                action_1(data, count)

            elif int(j) == 2:
                print_dict(action_2(data, count))

            elif int(j) == 3:
                dep = action_2(data, count)
                action_3(dep)

            else:
                print("Wrong command\n")
        except ValueError:
            print("Only numbers are acceptable")


    print('Что вы хотите сделать? \n',
          '1: Вывести в понятном виде иерархию команд,'
                                        ' т.е. департамент и все команды, которые входят в него\n'
          '2: Вывести сводный отчёт по департаментам: название, численность, "вилка" зарплат , средняя зарплата\n'
          '3: Сохранить сводный отчёт из предыдущего пункта в виде csv-файла.\n'
          'Напишите 1, 2 или 3\n')
    data, count = read_file()
    get_inquery(data, count)
