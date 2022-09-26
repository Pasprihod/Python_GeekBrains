#Задание 1
print('Задание 1')
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def set_date(cls, text):
        if Date.date_validating(text)[0]:
            day, month, year = Date.date_validating(text)[1]
            return Date(day, month, year)
        else:
            print('Enter correct date')

    @staticmethod
    def date_validating(text):
        text_split = text.split('-')
        error_flag = False
        if len(text_split) != 3:
            error_flag = True
        else:
            for el in text_split:
                if el.isdigit() == False:
                    error_flag = True
                    break

        if error_flag:
            return False, ' '
        else:
            day, month, year = map(int, text_split)
            if day in range(1, 29) and month == 2 or day in range(1, 31) and month in [4, 6, 9, 11] or day in range(1, 32) and month in [1, 3, 5, 7, 8, 10, 12]:
                return True, [day, month, year]
            else:
                return False, ' '

date1 = Date.set_date('31-05-2000')
print(date1.day, date1.month, date1.year)
print('*'*50)

# Задание 2
print('Задание 2')
class DivisionByNull(Exception):
    def __init__(self, text):
        self.text = text

a = input('Enter divisible ')
b = input('Enter divider ')
try:
    a_int = int(a)
    b_int = int(b)
    if b_int == 0:
        raise DivisionByNull('Division by 0!!!')
except ValueError:
    print('Enter integer')
except DivisionByNull as err:
    print(err)
else:
    print(f'Well done {a_int/b_int}')

print('*'*50)

# Задание 3
print('Задание 3')
class OnlyNumber(Exception):
    def __init__(self, text):
        self.text = text

    @staticmethod
    def execution(number_str):
        if number_str.isdigit():
            return True
        else:
            return False

number_list = []
while True:
    el = input("Enter element or stop for finish")
    if el == 'stop':
        break
    else:
        err = OnlyNumber('Enter integer')
        if OnlyNumber.execution(el):
            number_list.append(int(el))
        else:
            print(err)
print(number_list)
print('*'*50)

# Задание 3.1
print('Задание 3.1')
class OnlyNumber(Exception):
    def __init__(self, text):
        self.text = text

number_list = []
while True:
    try:
        el = input("Enter element or stop for finish")
        if el == 'stop':
            break
        else:
            if el.isdigit():
                number_list.append(int(el))
            else:
                raise OnlyNumber('Enter integer')
    except OnlyNumber as err:
        print(err)
print(number_list)

print('*'*50)


# Задание 4
print('Задание 4')

class DiagnosticEquipment:
    ''' Задача: распределить поступающее оборудование
    для лучевой диагностики (МРТ, КТ) по клиникам.
     Клиники выставляют запрос на требуемое оборудование.
     По нему идет сверка с типом оборудования и выполняется
     передача. Данные списка с оборудованием и клиниками
     с запросом или оборудованием записываются в файл'''

    clinic = None # Название клиники, куда поставлено оборудование
    eq_dict = {} # словарь с порядковым номером, наименованием и параметрами оборудования
    count = 0

    def __init__(self, manufacturer, model, eq_type, year, cost):
        eq_type, year, cost = DiagnosticEquipment.set_data(eq_type, year, cost)
        self.model = model
        self.manufacturer = manufacturer
        self.eq_type = eq_type # МРТ или КТ
        self.year = year
        self.cost = cost

    @staticmethod
    def write_in_file(): # запись в файл (обновление файла) данных по оборудованию
        with open('Equipment list', 'w', encoding='utf-8') as f:
            list_str = ''
            for i in DiagnosticEquipment.eq_dict.keys():
                list_str = ''
                for j in DiagnosticEquipment.eq_dict[i]:
                    list_str += str(j) + ', '
                f.write(f'{i} : {list_str[:-2]}\n')

    @staticmethod
    def set_data(eq_type, year, cost): # валидатор на общие параметры
        if eq_type.upper() not in ['MRI', 'CT']:
            print('Enter correct equipment type!')
            eq_type = None
        if type(year) != int:
            print('Year must be integer!')
            year = None
        if type(year) == int and year < 2010:
            print('Equipment is too old!')
            year = None
        if type(cost) != int:
            print('Cost must be integer!')
            year = None
        return eq_type, year, cost


class MRI(DiagnosticEquipment): #  класс МРТ

    def __init__(self, manufacturer, model, eq_type, year, cost, field_strength):
        super().__init__(manufacturer, model, eq_type, year, cost)
        field_strength = MRI.set_MRI_data(field_strength)
        self.field_str = field_strength
        self.clinic = DiagnosticEquipment.clinic  # название клиники, куда будет поставлен
        DiagnosticEquipment.count += 1
        self.number = DiagnosticEquipment.count
        DiagnosticEquipment.eq_dict[DiagnosticEquipment.count] = [self.eq_type, self.manufacturer, self.model,
                                                                  self.field_str, self.year, self.cost, self.clinic]
        DiagnosticEquipment.write_in_file()

    def transfer(self, clinic_name): # передача данного оборудования в клинику
        try:
            if Clinic.clinic_dict[clinic_name] == self.eq_type: # проверка, есть у клиники запрос на такое оборудование
                Clinic.clinic_dict[clinic_name] = [self.eq_type, self.manufacturer, self.model, self.field_str,
                                                   self.year, self.cost]
                self.clinic = clinic_name
                DiagnosticEquipment.eq_dict[self.number][6] = clinic_name
                DiagnosticEquipment.write_in_file()
                Clinic.write_Clinic_in_file()
            else:
                print(f'{clinic_name} does not need MRI')
        except KeyError:
            print('No such clinic. Enter correct clinic name.')

    @classmethod
    def set_MRI_data(cls, field_strength): # проверка спец. МРТ параметров
        if type(field_strength) == float or type(field_strength) == int:
            return field_strength
        else:
            print(('Enter correct field strength'))
            return None

    def __str__(self):
        return f'{self.manufacturer}, {self.model}, {self.field_str}, {self.year}, {self.clinic}'


class CT(DiagnosticEquipment):
    def __init__(self, name, manufacturer, eq_type, year, cost, slice_number):
        super().__init__(name, manufacturer, eq_type, year, cost)
        slice_number = CT.set_CT_data(slice_number)
        self.slice_number = slice_number
        self.clinic = DiagnosticEquipment.clinic  # название клиники, куда будет поставлен
        DiagnosticEquipment.count += 1
        self.number = DiagnosticEquipment.count
        DiagnosticEquipment.eq_dict[DiagnosticEquipment.count] = [self.eq_type, self.manufacturer, self.model,
                                                                  self.slice_number, self.year, self.cost, self.clinic]
        DiagnosticEquipment.write_in_file()

    def transfer(self, clinic_name):
        try:
            if Clinic.clinic_dict[clinic_name] == self.eq_type:
                Clinic.clinic_dict[clinic_name] = [self.eq_type, self.manufacturer, self.model, self.slice_number,
                                                   self.year, self.cost]
                self.clinic = clinic_name
                DiagnosticEquipment.eq_dict[self.number][6] = clinic_name
                DiagnosticEquipment.write_in_file()
                Clinic.write_Clinic_in_file()
            else:
                print(f'{clinic_name} does not need CT')
        except KeyError:
            print('No such clinic. Enter correct clinic name.')

    @classmethod
    def set_CT_data(cls, slice_number): # проверка спец. КТ параметров
        if type(slice_number) == int:
            return slice_number
        else:
            print(('Enter correct slice number'))
            return None

    def __str__(self):
        return f'{self.manufacturer}, {self.model}, {self.slice_number}, {self.year}, {self.clinic}'


class Clinic:
    count = 0
    clinic_dict = {}

    def __init__(self, name, request):
        self.name = name
        self.request = request  # запрос на поставку оборудования MRI, CT, US
        Clinic.count += 1
        Clinic.clinic_dict[self.name] = self.request

    def __str__(self):
        return f'{self.name}, request for {self.request}'

    @classmethod
    def write_Clinic_in_file(clc):
        with open('Clinic list', 'w', encoding='utf-8') as f:
            list_str = ''
            for i in clc.clinic_dict.keys():
                list_str = ''
                for j in clc.clinic_dict[i]:
                    list_str += str(j) + ', '
                f.write(f'{i} : {list_str[:-2]}\n')


mri1 = MRI('GE', 'Prizma', 'MRI', 2020, 1000000, 1.5)
mri2 = MRI('Philips', 'Achieva', 'MRI', 2015, 1500000, 3)
mri3 = MRI('Canon', 'Titan', 'MRI', 2015, 2500000, 3)
ct1 = CT('Canon', 'Aquilion', 'CT', 2018, 500000, 12.8)
clinic1 = Clinic('NII Burdenko', 'CT')
ct1.transfer('NII Burdenko')

# print(MRI.eq_dict)

print('*' * 50)

# Задание 5
print('Задание 5')
class ImNum:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f'{self.real} + {self.imag}*i'
        else:
            return f'{self.real} - {-self.imag}*i'

    def __add__(self, other):
        return ImNum(self.real+other.real, self.imag+other.imag)

    def __mul__(self, other):
        return ImNum(self.real*other.real-self.imag*other.imag, self.imag*other.real + self.real*other.imag)

a = ImNum(2, 0)
b = ImNum(1, 0)
print(a*b)
print(a+b)

print('*'*50)
