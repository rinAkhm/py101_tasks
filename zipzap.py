"""
Программа выводит на экран числа от 1 до 100 включительно, с новой строки.

Если число кратно трём, то вместо этого числа программа выводит слово "zip"
Если чисто кратно пяти, то вместо этого числа выводится слово "zap"
Если число кратно пятнадцати, то вместо этого числа выводится слово "zip-zap"

Тебе может понадобиться цикл for и ветвления
"""

if __name__ == '__main__':
    for number in range(1,101):
        if number%3==0 and number%5==0:
            print(f'zip-zap')
        elif number%3==0:
            print(f'zip')
        elif number%5==0:
            print(f'zap')  
        else:
            print(f'{number}')
    
        
