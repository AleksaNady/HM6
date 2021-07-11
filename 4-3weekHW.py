class Car:
    """класс машина"""

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'new car: {self.name} (цвет {self.color})  - {self.is_police}')

    def go(self):
        print(f'{self.name}: машина поехала')
    def stop(self):
        print(f'{self.name}: машина остановалиась')
    def turn(self, direction):
        print(f'{self.name}: машина повернула {"налево" if direction == 0 else "направо"}.')
    def show_speed(self):
        return f"{self.name}: скорость автомобиля: {self.speed}."

class TownCar(Car):
    """Городской автомобиль"""
    def show_speed(self):
        return f"{self.name}: скорость автомобиля: {self.speed}. превышение скорости!" \
            if self.speed > 60 else f"{self.name}: скорость автомобиля {self.speed}"

class WorkCar(Car):
    """Грузовой автмомибль"""
    def show_speed(self):
        return f"{self.name}: скорость автомобиля: {self.speed}. превышение скорости!" \
            if self.speed > 40 else f"{self.name}: скорость автомобиля {self.speed}"

class SportCar(Car):
    """Спортивный автомобиль"""

class PoliceCar(Car):
    """Полицейский автомобиль"""
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)

police_car = PoliceCar('Форд', 'белая', 80)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work_car = WorkCar("Фура","белый", 40)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()

print()
sport_car = SportCar("Болид","черный", 120)
sport_car.go()
sport_car.turn(0)
print(sport_car.show_speed())
sport_car.stop()
print()

town_car = TownCar("Жук", "зеленый", 50)
town_car.go()
town_car.turn(1)
town_car.turn(0)
print(town_car.show_speed())
town_car.stop()



