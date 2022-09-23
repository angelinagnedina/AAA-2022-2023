import csv


def hierarchy() -> None:
    """
    Функция, которая выводит иерархию команд.
    """
    with open('../Files_with_data/Corp_Summary.csv', newline='') as data_csv:
        data = csv.reader(data_csv, delimiter=';')
        departments = {}
        next(data)

        for row in data:
            if departments.get(row[1]) is None:
                departments[row[1]] = []
            departments[row[1]].append(row[2])

        for key, value in departments.items():
            print(f'Название департамента - {key}. Команды, входящие в него: ', end='')
            print(*set(value), sep=', ')


def report(for_second_option: bool = True) -> None:
    """
    :param for_second_option: True, если используется для опции 2, иначе False
    """
    with open('../Files_with_data/Corp_Summary.csv', newline='') as data_csv:
        data = csv.reader(data_csv, delimiter=';')
        departments = {}
        statistics = {}
        next(data)

        for row in data:
            if departments.get(row[1]) is None:
                departments[row[1]] = []
            departments[row[1]].append(int(row[-1]))

        for key, value in departments.items():
            statistics[key] = [len(value), str(min(value)) + '-' + str(max(value)), sum(value)//len(value)]
            if for_second_option:
                print(f'Название департамента - {key}. Численность - {statistics[key][0]}.',
                      f'Вилка зарплат - {statistics[key][1]}.',
                      f'Средняя зарплата - {statistics[key][-1]}.')

        if not for_second_option:
            with open('../Files_with_data/file_with_report.csv', 'w', newline='') as result:
                result_writer = csv.writer(result, delimiter=' ')
                result_writer.writerow(['Название департамента', 'Численность',
                                        'Вилка зарплат', 'Средняя зарплата'])
                for key, value in statistics.items():
                    result_writer.writerow([key, *value])

                print('Данные лежат в ../Files_with_data/file_with_report.csv')


if __name__ == '__main__':
    options = {
        1: ('Вывести в понятном виде иерархию команд, т.е. департамент '
            'и все команды, которые входят в него.'),
        2: 'Вывести сводный отчёт по департаментам: название, численность,'
           '"вилка" зарплат в виде мин – макс, среднюю зарплату.',
        3: 'Сохранить сводный отчёт из предыдущего пункта в виде csv-файла.'
    }
    print('Выберите действие из следующих:')
    print(*[f'{key}. {value}' for key, value in options.items()], sep='\n')
    selected = int(input())

    while not 0 < selected < 4:
        print('Выберите число от 1 до 3.')
        selected = int(input())

    if selected == 1:
        hierarchy()
    if selected == 2:
        report()
    if selected == 3:
        report(False)
