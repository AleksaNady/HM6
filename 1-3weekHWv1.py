import time
import itertools

class TrafficLight:
    __color = [['red', [7, 31]], ['yellow', [2, 33]], ['green', [5, 32]]]

    def running(self):
        for light in itertools.cycle(self.__color):
            print(f'\r\033[{light[1][1]}m\033[1n{light[0]}\033[0m', end='')
            time.sleep(light[1][0])

trafficlight_1 = TrafficLight()
trafficlight_1.running()
