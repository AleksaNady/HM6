class Worker:
    """Класс работника"""
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._incom = {"wage":wage, "bonus":bonus}
        """создание конструктора с параметрами """
class Position(Worker):
    """Класс позиции"""
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._incom.values())}"
    """ Вычисляет полный доход"""

worker_1 = Position("Сорокина", "Елена", "бухгалтер", 50000, 125000)
print(worker_1.get_full_name())
print(worker_1.position)
print(worker_1.get_full_profit())


