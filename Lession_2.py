# Задание 1
print('Задание 1')
l = [87, True, 0.0001, 'qqqqq', ('q','w'), {'a','s','d','f'}]
for i in l:
    print(f'{i} - {type(i)}')

print('='*50)

# Задание 2
print('Задание 2')
l = [87, True, 0.0001, 'qqqqq', ('q','w')]
print(l)
for i in range(0, len(l),2):
    if i != len(l)-1:
        l[i],l[i+1] = l[i+1], l[i]
    else:
        break
print(l)
print('='*50)

# Задание 3
print('Задание 3')
#Решение через list:
mes_list = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
vg_list = ['Зима', 'Весна', 'Лето', 'Осень']
mes = int(input('Введите номер месяца года'))
i = 0
for el in mes_list:
    if mes in el:
        print(vg_list[i])
        break
    else:
        i += 1

#Решение через dict:
vg_dict = {'Зима' : [1, 2, 12],
        'Весна' : [3, 4, 5],
        'Лето' : [5, 6, 7],
        'Осень' : [9, 10, 11]}
mes = int(input('Введите номер месяца года'))
for el in vg_dict:
    if mes in vg_dict[el]:
        print(el)
        break
print('='*50)

# Задание 4
print('Задание 4')
slova = input('Введите несколько слов через пробел').split()
for i,el in enumerate(slova,1):
    print(f'{i} - {el[:10]}')
print('='*50)

# Задание 5
print('Задание 5')
rating = [10, 10, 9, 8, 6, 4, 3, 2]
print(rating)
new = int(input('Введите цифру рейтинга от 0 до 10'))

if rating.count(new):
    rating.insert(rating.index(new) + rating.count(new), new)
else:
    i = 0
    while rating[i] > new:
        i +=1
        if i == len(rating):
            break
    rating.insert(i, new)
print(rating)

print('='*50)

# Задание 6
print('Задание 6')
i = 1
list_product = []
vvod = 'y'
while vvod == 'y':
    print('Введите параметры товара:')
    product = {'Название': input('Название'),
             'Цена': float(input('Цена')),
             'Количество': float(input('Количество')),
             'Ед': input('Ед') }

    vvod = input('Будете добавлять товар? y/n')
    list_product.append((i,product))
    i += 1
key_list = list(product.keys())
analitics = {key: [] for key in key_list}

for el in list_product:
    for el1 in key_list:
        analitics[el1].append(el[1].get(el1))
print(analitics)
print('='*50)