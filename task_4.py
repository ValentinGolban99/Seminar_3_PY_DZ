# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите челое число: '))

def binar(n): 
    if(n > 1):
        binar(n // 2)
    print(n % 2, end = '')
     
binar(num)


# Вспомнил курс про информатику и информатику))




