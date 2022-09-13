# Задание 1
print('Задание 1')
with open('text1.txt', 'w', encoding='utf-8') as f:
    while True:
        str_data = input('Введите данные. Для окончания ввода передайте пустую строку')
        if str_data == '':
            break
        else:
            f.write(f'{str_data}\n')

print('*'*50)

# Задание 2
print('Задание 2')

with open('text2.txt', 'w+', encoding='utf-8') as f:
    while True:
        str_data = input('Введите данные. Для окончания ввода передайте пустую строку')
        if str_data == '':
            break
        else:
            f.write(f'{str_data}\n')
    f.seek(0)
    lines = f.readlines()
print('Количество строк - ', len(lines))
i=1
for el in lines:
    print(f'{i}-я строка: {el[:len(el)-1]}. Количество символов: {len(el)-1} ')
    i+=1
print('*'*50)

#Задание 3
print('Задание 3')
with open('text3_фамилии_оклады.txt', 'w+', encoding='utf-8') as f:
    sotrudniki = ['Иванов 19356\n',
                  'Петров 45000\n',
                  'Сидоров 11000.43\n',
                  'Соколов 200000.73\n',
                  'Щетина 13400\n',
                  'Перепрыгничерезсвечку 16999\n',
                  'Непейпиво 14356\n',
                  'Денежка 21356\n',
                  'Попеску 34998\n',
                  'Любимый 89356\n']
    f.writelines(sotrudniki)
    f.seek(0)
    dohod = []
    print('Сотрудники, у которых доход менее 20000:')
    for el in f:
        familiya_dohod = el.split()
        try:
            dohod_1 = float(familiya_dohod[1])
            dohod.append(dohod_1)
            if dohod_1 < 20000:
                print(familiya_dohod[0])
        except:
            print('Ошибка при вводе дохода в строке ', el, 'Рассчет неверный')
    print('Средний доход ', round(sum(dohod)/len(dohod), 2))


print('*'*50)

# Задание 4
print('Задание 4')
with open('text4_числа на английском.txt', 'w+', encoding='utf-8') as f:
    numbers_english = ['One-1\n','Two-2\n','Three-3\n','Four-4\n']
    f.writelines(numbers_english)
    f.seek(0)
    number_list_english = f.readlines()
    number_dict = {'One': 'Один',
                   'Two': 'Два',
                   'Three': 'Три',
                    'Four': 'Четыре'}
    number_list_russian = []
    for el in number_list_english:
        number_str = el.split('-')# разделитель -
        for i in number_dict.keys():
            if number_str[0] == i:
                number_list_russian.append(f'{number_dict.get(i)}-{number_str[1]}')
with open('text4_числа на русском.txt', 'w', encoding='utf-8') as f:
    f.writelines(number_list_russian)
print('*'*50)

# Задание 5
print('Задание 5')
with open('text5_числа через пробел.txt', 'w+', encoding='utf-8') as f:
    f.write('2 -5 3 0 10 4.2')
    f.seek(0)
    print('Числа: ',f.read())
    f.seek(0)
    print('Сумма: ',sum(map(float,f.read().split())))
print('*'*50)

# Задание 6
print('Задание 6')
with open('text6_предметы и часы.txt', 'w+', encoding='utf-8') as f:
     predmety = ['Информатика 100л 50с 20лаб\n',
                 'Математика 50л 50с \n',
                 'Физика 100л 100с 50лаб\n',
                 'Русский язык 30л 30с\n']
     f.writelines(predmety)
     f.seek(0)
     predmety_dict = {}
     for el in f:
         # Формирование списка количества часов для каждого
         # предмета для общего случая записи в строке (вырезание только чисел из строки)
         numbers_list = [] #список из количества лекций, семинаров, лаб
         flag = 1 # индикатор ожидания числа для записи
         number = ''  # число, которое вырезается из строки
         for i in el: # анализ строк
             if i.isdigit():
                 number += i # формируем число в строковом виде
                 flag = 0 # запись числа началась
             elif i.isdigit() == False and flag == 0: # условие для прекращения записи числа
                 numbers_list.append(number) # добавляем сформированное число в список для текущего предмета
                 flag = 1 # остановка записи, переход в ожидание нового числа
                 number = ''  # обнуление, подготовка для записи

         # Формирование правильного названия предмета (если состоит больше, чем из одного слова)
         name = ''
         name_list = el.split()
         for el1 in name_list:
             if el1.isalpha():
                 name += el1 + ' '

         predmety_dict[name[:-1]] = sum(map(int,numbers_list))

     print(predmety_dict)

print('*'*50)

# Задание 7
print('Задание 7')

from statistics import mean
import json

with open('text7_фирмы_форма_выручка_издержки.txt','w', encoding='utf-8') as f:
    firms = ['Рога и копыта ООО 500 10000\n',
             'НПФ Аз 333 ЗАО 1000 1\n',
             'Сбербанк АО 10000000 700000\n',
             'Вася Пупкин ООО 10 10']
    f.writelines(firms)

with open('text7_фирмы_форма_выручка_издержки.txt', 'r', encoding='utf-8') as f:
    firms_dict_profit = {}
    firms_dict_lose = {}
    firms_list_final = []
    for el in f: # проход по строчкам файла
        firms_list_str = el.split()
        profit = float(firms_list_str[-2]) - float(firms_list_str[-1]) # рассчетные поля - 2 последних
        name = ' '.join(firms_list_str[:-3]) # формируем название фирмы без учета трех последних значений
        if profit > 0:
            firms_dict_profit[name] = profit
        else:
            firms_dict_lose[name] = profit

    firms_list_final.append(firms_dict_profit)
    firms_list_final.append({'Average profit': round(mean(firms_dict_profit.values()), 2)})
    firms_list_final.append(firms_dict_lose)
    print(firms_list_final)

with open('text7_фирмы_форма_выручка_издержки.json', 'w', encoding='utf-8') as f:
    json.dump(firms_list_final, f, ensure_ascii=False) # чтобы записывались адекватно русские буквы

print('*'*50)