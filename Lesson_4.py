# Задание 1
from sys import argv
'''
argv[1] - выработка, час
argv[2] - ставка, руб/час
argv[3] - премия, руб
'''
print(f'Зарплата сотрудника - {float(argv[1])*float(argv[2])+float(argv[3])} руб')

# Задание 2
print('Задание 2')
li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 155]
li_new = [li[i] for i in range(1,len(li)) if li[i] > li[i-1]]
print(li)
print(li_new)
print('*'*50)

# Задание 3
print('Задание 3')
li = [el for el in range(20,241) if el % 20 == 0 or el % 21 == 0]
print(li)
print('*'*50)

# Задание 4
print('Задание 4')
li =  [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
li_new = [el for el in li if li.count(el) == 1]
print(li_new)
print('*'*50)

#Задание 5
print('Задание 5')
from functools import reduce
def product(n1,n2):
    return n1*n2

print(reduce(product, [el for el in range (100,1001,2)]))
print('*'*50)

# Задание 6
print('Задание 6')
from itertools import count, cycle
# Итератор с count
while True:
        try:
            start = int(input('Введите целое положительное число, с которого начинаем отсчет'))
            finish = int(input('Введите целое положительное число, на котором прерываем отсчет'))
            break
        except ValueError:
            print('Введите корректные числа')
iter_count = []
for el in count(start):
    if el > finish:
        break
    else:
        iter_count.append(el)
print(f'Итератор count {iter_count}')

# Итератор cycle

while True:
        try:
            number = int(input('Введите число проходов '))
            li = (input('Введите подряд элементы списка'))
            break
        except ValueError:
            print('Введите корректное число')
iter_cycle = []
i = 1
for el in cycle(li):
    if i > number:
        break
    else:
        iter_cycle.append(el)
        i += 1
print(f'Итератор cycle {iter_cycle}')
print('*'*50)

# Задание 7
print('Задание 7')
def fact(n):
    if n <= 1:
        yield 1
    else:
        f = 1
        for i in range(2,n+1):
            f = f*i
            yield f

while True:
        try:
            n = int(input('Введите целое неотрицательное число для подсчета факториала '))
            break
        except ValueError:
            print('Введите корректное число')

print(fact(n))
if n == 0:
    print('0! = 1')
elif n == 1:
    print('0! = 1')
    print('1! = 1')
else:
    print('0! = 1')
    print('1! = 1')
    i = 2
    for el in fact(n):
        print(f'{i}! = {el}')
        i += 1
print('*'*50)