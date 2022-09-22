# Задание 1
print('Задание 1')

class Matrix:
    def __init__(self,m):
        self.m = m
        self.row_number = len(m)
        self.column_number = len(m[0])

    def __str__(self):
        matrix_string = [[str(el) for el in row] for row in self.m]
        lens_max =[max(map(len, col)) for col in zip(*matrix_string)]
        table = ''
        for i in range(self.row_number):
            s = '|'
            for j in range(self.column_number-1):
                s += matrix_string[i][j]+' '*(lens_max[j]-len(matrix_string[i][j])+3)
            table += s + matrix_string[i][-1] + ' '*(lens_max[-1]-len(matrix_string[i][-1]))+'|\n'
        len_row_max = max(map(len, table.split('\n')))
        table_final = '_'*len_row_max+'\n'+ ('\n'+'_'*len_row_max+'\n').join(table.split('\n'))+'\n'


        return table_final
    def __add__(self, other):
        if self.row_number == other.row_number and self.column_number == other.column_number:
            print('Add resultant matrix:')
            m_rez=[[self.m[i][j]+other.m[i][j] for j in range(self.column_number)] for i in range(self.row_number)]
            return Matrix(m_rez)
        else:
            return 'Method Add: Matrix size must be the same'

m1 = Matrix([[100, 1182],[3, 4],[5, 6]])
print(m1)
m2 = Matrix([[6, 2],[0, 4],[5, -10]])
print(m2)
print(m1+m2)

print('*'*50)

# Задание 2.1
print('Задание 2.1')

class Clothes():
    cons_amount = 0 # общее количество потраченного материала

    def consumption(self):
        return Clothes.cons_amount

class Coat(Clothes):
    def __init__(self, v):
        self.size = v

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, v):
        if v <= 60: # максимальный размер
            self.__size = v
        else:
            self.__size = 0
            print('Too huge!')

    def consumption(self):
        self.cons_amount = round(self.__size/6.5 + 0.5, 2) if self.size > 0 else 0
        Clothes.cons_amount += self.cons_amount # добавка к общему количеству материала

class Suit(Clothes):
    def __init__(self, h):
        self.size = h

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, h):
        if h <= 2.5:
            self.__size = h
        else:
            self.__size = 0
            print('Too huge!')

    def consumption(self):
        self.cons_amount = round(self.__size*2 + 0.3, 2) if self.size > 0 else 0
        Clothes.cons_amount += self.cons_amount


c1 = Coat(80)
c2 = Coat(40)
s1 = Suit(1.5)
c1.consumption()
c2.consumption()
s1.consumption()
print(c1.cons_amount)
print(c2.cons_amount)
print(s1.cons_amount)
print(Clothes.cons_amount)
print('*'*50)

# Задание 2.2
print('Задание 2.2')
from abc import ABC, abstractmethod
class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

class Coat(Clothes):
    def __init__(self, v, cons_amount=0):
        self.size = v
        self.cons_amount = cons_amount # потраченная ткань

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, v):
        if v <= 60: # максимальный размер
            self.__size = v
        else:
            self.__size = 0
            print('Too huge!')

    def consumption(self):
        self.cons_amount = round(self.__size/6.5 + 0.5, 2) if self.size > 0 else 0

    def __add__(self, other):
        return Coat(self.size, self.cons_amount + other.cons_amount)

    def __str__(self):
        return str(self.cons_amount)

class Suit(Clothes):
    def __init__(self, h, cons_amount=0):
        self.size = h
        self.cons_amount = cons_amount # потраченная ткань

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, h):
        if h <= 2.5:
            self.__size = h
        else:
            self.__size = 0
            print('Too huge!')

    def consumption(self):
        self.cons_amount = round(self.__size*2 + 0.3, 2) if self.size > 0 else 0

    def __add__(self, other):
        return Suit(self.size, self.cons_amount + other.cons_amount)

    def __str__(self):
        return str(self.cons_amount)

c1 = Coat(80)
c2 = Coat(40)
s1 = Suit(1.5)
c1.consumption()
c2.consumption()
s1.consumption()
print(c1.cons_amount)
print(c2.cons_amount)
print(s1.cons_amount)
print(c1+s1+с2)

print('*'*50)

# Задание 3
print('Задание 3')
class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return str(self.cell)

    def __add__(self, other):
        return Cell(self.cell+other.cell)

    def __sub__(self, other):
        return Cell(self.cell - other.cell) if self.cell >= other.cell else 'The first cell must be bigger!'

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def make_order(self, n):
        num = self.cell
        string = ('*'*n + '\n')*(num // n) + '*'*(num % n)
        print(string)
c1=Cell(10)
c2=Cell(8)
print(c2-c1)
print(c1*c2)
print(c2 / c1)
c1.make_order(3)
print('-'*50)