# Задание 1
print('Задание 1')
import time
from itertools import cycle

class TrafficLight:

    __time_dict = {'red': 7, 'yellow': 2, 'green': 3} # время каждого состояния

    def __init__(self):
        self.color = input('Введите стартовый цвет светофора (red, yellow, green)')
        self.running()

    def running(self):
        light_list = ['red', 'yellow', 'green']
        while light_list[0] != self.color.lower():
            light_list.insert(0, light_list.pop()) # формирование списка цветов, где задан стартовый цвет
        n = int(input('Введите количество циклов '))
        i = 1
        for el in cycle(light_list):
            if i > n*len(light_list): # именно циклы, а не повторения
                break
            print(el)
            time.sleep(TrafficLight.__time_dict.get(el))
            i += 1
t1 = TrafficLight()

print('*'*50)

# Задание 2
print('Задание 2')
class Road:
    __density = 25 # kg/cm/m^2
    __thickness = 5 # сm
    def __init__(self, lenght, width):
        self.__lenght = lenght
        self.__width = width
        self.__mass = self.__lenght*self.__width*Road.__thickness*Road.__density
        print(f'Длина дороги - {self.__lenght} м, Ширина дороги - {self.__width} м')
        print(f'Масса асфальта - {self.__mass} кг')

r1 = Road(10000,10)
print('*'*50)

# Задание 3
print('Задание 3')
class Worker:
    def __init__(self, name, surname, wage, bonus):
        self.name = name
        self.surname = surname
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def __init__(self, name, surname, wage, bonus):
        super().__init__(name, surname, wage, bonus)

    def get_full_name(self):
        print(f'{self.surname} {self.name}')
    def get_total_income(self):
        print(f'Total income - {sum(self._income.values())}')

pos1 = Position('Pavel','Sokolov', 100000, 300000)
pos1.get_full_name()
pos1.get_total_income()
print('*'*50)

# Задание 4
print('Задание 4')
class Car:
    _is_police = False
    _go_flag = False # Индикатор машина едет/стоит. Изначально она стоит
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = Car._is_police
        self.go_flag = Car._go_flag

    def go(self):
        if not self.go_flag:
            print('Command Go: Car has started')
            self.go_flag = True
        else:
            print('Command Go: Car is on the way already!')

    def stop(self):
        if self.go_flag:
            print('Command Stop: Car has stopped')
            self.go_flag = False
        else:
            print('Command Stop: Car is not driving!')

    def turn(self, direction):
        if self.go_flag:
            print(f'Command Turn: Car has turned to the {direction}')
        else:
            print('Command Turn: Car is not driving')

    def show_speed(self):
        if self.go_flag:
            print(f'Speed - {self.speed} km/h')
        else:
            print('Command show_speed: Car is not driving!')

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
    def show_speed(self):
        super().show_speed()
        if self.go_flag and self.speed > 60:
            print('OVERSPEED 60 km/h!!!')

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
    def show_speed(self):
        super().show_speed()
        if self.go_flag and self.speed > 40:
            print('OVERSPEED 40 km/h!!!')
class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True

car1 = TownCar(90, 'white', 'Audi')
print(type(car1))
print(car1.__dict__)
car1.stop()
car1.go()
car1.go()
car1.turn('left')
car1.stop()
car1.turn('right')
car1.show_speed()
car1.go()
car1.show_speed()

car2 = WorkCar(50, 'Black', 'BMW')
print(type(car2))
print(car2.__dict__)
car2.stop()
car2.go()
car2.go()
car2.turn('left')
car2.stop()
car2.turn('right')
car2.show_speed()
car2.go()
car2.stop()
car2.show_speed()

car3 = PoliceCar(50, 'Black', 'BMW')
print(type(car3))
print(car3.__dict__)
car3.turn('right')

print('*'*50)

# Задание 5
print('Задание 5')
class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print(f'Запуск отрисовки для класса Pen, экземпляр - {self.title}')
class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки для класса Pencil, экземпляр -  {self.title}')
class Hadle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки для класса Hadle, экземпляр -  {self.title}')
pen1 = Pen('Pen1')
pen1.draw()
pencil1 = Pencil('Pencil1')
pencil1.draw()
print('*'*50)