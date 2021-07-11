""" Класс дорожного полотна """
""" длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна """
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

        """ :param
        length: Длина дорожного полотна в метрах
        width: Ширина дорожного полотна в метрах
        """

    def get_full_profit(self,weight=25, thickness=5):
        return f"{self._length} m * {self._width} m * {weight} kg * {thickness} sm =" \
               f"{(self._length * self._width * weight * thickness) / 1000} т"

road_1 = Road(5000, 20)
print(road_1.get_full_profit())