#Задание № 2
print('Задание № 2')
s = int(input('Введите количество секунд'))
h = s // 3600
m = (s % 3600) // 60
s = (s % 3600) % 60
print(f"{h} : {m} : {s}")
print('='*50)

#Задание № 3
print('Задание № 3')
n = input('Введите цифру n от 1 до 9')
print(f"n+nn+nnn = {n} + {n+n} + {n+n+n} = {int(n)+int(n+n)+int(n+n+n)}")
print('='*50)

#Задание № 4
print('Задание № 4')
n = int(input('Введите целое положительное число '))
max_number = 0
while n > 0:
   if max_number < n % 10:
       max_number = n % 10
   n = n // 10
print(max_number)
print('='*50)

#Задания № 5, 6
print('Задание № 5,6')
vyr = float (input('Введите значение выручки'))
izd = float (input('Введите значение издержек'))
if vyr - izd > 0:
   print(f"Прибыль - {round(vyr-izd, 2)}, Рентабельность - {round((vyr-izd)/vyr, 3)}")
   n = int (input('Введите численность сотрудников'))
   print(f"Прибыль на одного сотрудника - {round((vyr - izd) / n, 3)}")
else:
   print(f"Убыток - {izd-vyr}")
print('='*50)

#Задание № 7
print('Задание № 7')
d1 = float(input('Введите дистанцию за первый день, км '))
dn = float(input('Введите дистанцию, которую надо достичь, км '))
d = d1 # текущий результат спортсмена
n = 1 # номер дня
print('Результаты:')
print(f"{n}-й день: ", round(d, 2))
while d < dn:
   n = n + 1
   print(f"{n}-й день: ", round(d * 1.1, 2))
   d = d * 1.1
print(f"На {n}-ой день спортсмен достиг результата не менее {dn} км")
print('='*50)