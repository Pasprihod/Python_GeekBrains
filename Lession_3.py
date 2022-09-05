#Задание № 1
print('Задание № 1')

def a_del_b(a, b):
     try:
         return a / b
     except ZeroDivisionError:
         print('Деление на 0')

a = float(input('Введите число '))
b = float(input('Введите число '))
print(a_del_b(a,b))

print('='*50)

#Задание № 2
print('Задание № 2')

def data_user(name, surname, birth_date, city, email, phone):
     print(f'{name} {surname}, {birth_date}, {city}, {email}, {phone}')

data_user(name='Ivan', surname='Ivanov', birth_date='2000',city='Moscow',email='ivan@mail.ru',phone='(111)111-11-11')
print('='*50)

#Задание № 3
print('Задание № 3')
def my_func(n1,n2,n3):
    number_list = [n1, n2, n3]
    number_list.remove(min(number_list))
    return sum(number_list)
n1=float(input('Введите число'))
n2=float(input('Введите число'))
n3=float(input('Введите число'))

print(my_func(n1,n2,n3))
print('='*50)

#Задание № 4
print('Задание № 4')
def my_fun(x,y):
    x1=1
    for i in range(int(abs(y))):
        x1 *= 1/x
    return x1
x=float(input('Введите целое положительное число '))
y=float(input('Введите целое отрицательное число '))
print(my_fun(x,y))
print('='*50)

#Задание № 5
print('Задание № 5')
def my_sum(numbers_str, stop, stop_flag):
    numbers_str_list = list(numbers_str.split()) # разбиение строки на элементы, разделенные пробелом
    if stop_flag in numbers_str_list: # проверка списка строковых элементов на наличие стоп-символа
        stop_index = numbers_str_list.index(stop_flag) # индекс стоп-сигнала в списке строковых элементов
        stop = True # необходимость заканчивать цикл
        numbers_str_list = numbers_str_list[:stop_index] # удаление строковых элементов, начиная со стоп-символа
    numbers_list = map(int, numbers_str_list) # перевод строковых элементов в числовые
    return sum(numbers_list), stop

stop = False # стоп - сигнал
stop_flag = 's' # стоп-символ в строке ввода
sum_all = 0 # результирующая сумма
while stop == False:
    numbers_str = input(f'Введите числа через пробел, для окончания ввода введите {stop_flag}')
    summa, stop = my_sum(numbers_str, stop, stop_flag)
    sum_all += summa
    print(sum_all)
print('='*50)

#Задание № 6
print('Задание № 6, 7')
def int_func(words_list):
    '''
    Принимает список слов из маленьких букв, выдает строку
    из тех же слов, но с заглавной буквы
    :param words_list: список слов с маленькой буквы
    :return: список слов с заглавной буквы
    '''
    words_title = ''
    for el in words_list:
        words_title += el.title() + ' '
    return words_title
flag = False # верно ли введены слова
while flag == False:
    words = input('Введите слова из маленьких латинских букв через пробел')
    char_range = [i for i in range(97,123)]
    char_range.append(ord(' ')) # формирование списка кодов
    # из ASCII-таблицы допустимых символов (маленькие
    # латинские буквы и пробел) для проверки на правильность ввода
    for i in words: #посимвольная проверка
        if ord(i) not in char_range:
            print('Введите слова правильно!')
            flag = False
            break
        else:
            flag = True
words_list = words.split()
print(int_func(words_list))
print('='*50)