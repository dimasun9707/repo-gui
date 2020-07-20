# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
#
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} в движении!'.format(self.name))

    def stop(self):
        print('{} Останавливается'.format(self.name))

    def turn(self, direction):
        print('{} поворачивает {}!'.format(self.name, direction))

    def show_speed(self):
        print('Актуальная скорость:', self.speed)

class TownCar(Car):
    def show_speed(self):
        print('Актуальная скорость городской машины', self.speed)
        if self.speed > 60:
            print('Вы превысили максимально разрешенную скорость')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print('Актуальная скорость рабочей машины', self.speed)
        if self.speed > 40:
            print('Вы превысили максимально разрешенную скорость')

class PoliceCar(Car):
    pass


sport_car = SportCar(140, 'Красная', 'Спортивная машина', False)
town_car = TownCar(80, 'Серая', 'Городская машина', False)
work_car = WorkCar(70, 'Желтая', 'Рабочая машина', False)
police_car = PoliceCar(180, 'Синяя', 'Полицейская машина', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('На право')
