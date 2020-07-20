# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)и дохода с учетом премии (get_total_income).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income_wage = income['wage']
        self._income_bonus = income['bonus']


class Position(Worker):
    def get_full_name(self):
        full_name = self.name + self.surname + self.position
        return full_name

    def get_total_income(self):
        total_income = self._income_wage + self._income_bonus
        return total_income


pos = Position('Pavel ', 'Simakin ', 'Junior', {"wage": 18000, "bonus": 30000})
pos.get_full_name()
pos.get_total_income()
print(pos.get_full_name())
print(pos.get_total_income())



