
class Stationery:
    """Класс канцелярские принадлежности"""
    def __init__(self, title="метод draw"):
        self.title = title

    def draw(self):
        print(f'запуск отрисовки: {self.title}')

class Pen(Stationery):
    """Класс ручка"""
    def draw(self):
        print(f"пишет, ”{self.title}” ручка!")

class Pencil(Stationery):
    """Класс карандаш"""
    def draw(self):
        print(f'чертит, ”{self.title}” карандаш!')

class Handle(Stationery):
    """Класс ручка"""
    def draw(self):
        print(f'рисует, ”{self.title}” маркер!')

stationery_1 = Stationery()
stationery_1.draw()
pen = Pen("Attache")
pen.draw()
pencil = Pencil("TM")
pencil.draw()
marker = Handle("Edding 380")
marker.draw()
