# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 




num_k = int(input('Введите число: '))

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

list_ = []
for i in range(1, num_k + 1):
    list_.append(fib(i))

list_2 = []
for i in range(1, num_k + 1):
    list_2.append(fib(i) * -1)

print(list(reversed(list_2)) + list_)

# Воспользовался рекурсией из лекции.
# У меня получилось только в таком виде. С нулем туплю)