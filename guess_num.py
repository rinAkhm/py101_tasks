
from random import randint

"""
Программа генерирует число от 0 до 1_000_000 и предлагает угадать его.
Программа должна приветствовать пользователя и считывать число с клавиатуры
Если число меньше загаданного, то программа выводит сообщение о том, что число
меньше
Если больше загаданного, то программа выводит сообщение о том, что больше
Программа должна выводить сообщения-предупреждения, если:
* пользователь ввёл не число
* число не входит в обозначенный в условии диапазон
Если пользователь ничего не ввёл/ввёл "exit", то происходит выход из программы.
Тебе может понадобится модуль random, цикл while и ветвления
"""


if __name__ == '__main__':
    digits = []
    for digit in range(0, 10):
        digits.append(randint(1,1_000_001))
    digits.sort()
    rnd_number = digits[randint(0,1)]
    print('Please, input your number. you can input word "exit" for exit from program or tap button "Enter" on keyboard')
    while(True):
        number = input()
        if (number.lower() == 'exit' or number == ''):
            print('You out from programs. Goodbay!')
            break
        elif(number.isdigit()):
            if(int(number) > 0 and int(number) < 1_000_001):
                if int(number) < rnd_number:
                    print(f'this number is more than {number}')
                elif int(number) > rnd_number:
                    print(f'this number is lower than {number}')
                else:
                    print('You can found number, congratulations!')
            else:
                print('you need to enter a number from 1 to 1000000')
        else:
            print('you need to enter only a number')