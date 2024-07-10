def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return str(a) + str(b)
    except BaseException as exp_:
        print(f'Понятия не имею какая тут могла ошибка произойти?!! Разбирайтесь сами!\n'
              f'Вот вам данные ошибки: {exp_.__class__}, {exp_.args}')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
