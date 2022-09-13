def step2_umbrella():
    answer = 'Совет, конечно, хороший, но зонт у утки украли в баре. \nНе ходите в бары на Рубинштейна...'

    print(answer)


def step2_no_umbrella():
    answer = ('А утка-то живёт в Питере, \nИ из-за твоего совета её дождём смыло в Неву. \nНе давай больше '
              'советов... ')

    print(answer)


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
