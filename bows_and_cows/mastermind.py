# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       проверяем что пользователь ввел допустимое число (4 цифры, все цифры разные, не начинается с 0)
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем (вывод на консоль и запрос ввода от пользователя) делать в 01_mastermind.py.
# Движок игры реализует только саму функциональность игры. Разделяем: mastermind_engine работает
# только с загаданным числом, а 01_mastermind - с пользователем и просто передает числа на проверку движку.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT
import time
from mastermind_engine import make_number, check_number


def game_start():
    make_number()
    print('Я загадываю число...')
    time.sleep(1)
    print('Поехали!')


def game_restart(_step):
    allow_answer = ['да', 'нет']
    print('Количество шагов: {}'.format(step))
    print('Поздравляю!\nВы отгадали число которое я загадал!')
    answer = input('Хотите еще партию?\nОтвечайте только да или нет: ')
    while answer not in allow_answer:
        answer = input('Отвечайте только да или нет:')
    if answer == 'да':
        game_start()


def uncorrected_number(_numb):
    test_str = ''
    allow_number = []
    for i in range(0, 10):
        allow_number.append(str(i))
    if len(user_number) == 4:
        for i, sign in enumerate(user_number):
            if i == 0:
                if sign in allow_number[1:]:
                    test_str += sign
            else:
                if sign in allow_number:
                    if test_str.find(sign) == -1:
                        test_str += sign
    if len(test_str) == 4:
        return False
    else:
        return True


game_start()
step = 0

while True:
    user_number = input('Введите ваше число: ')
    if uncorrected_number(user_number):
        print('Необходимо ввести четыре различные цифры. Первая должна быть отличная от нуля')
        continue
    bulls, cows = check_number(user_number)['bulls'], check_number(user_number)['cows']
    if bulls == 4:
        step += 1
        game_restart(step)
        step = 0
        break
    else:
        step += 1
        print('>быки - {},'.format(bulls), 'коровы - {}'.format(cows))

# зачет!