from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        vil = 100
        days = 0
        print(f'{self.name}, на нас напали!')

        while vil != 0:
            days+=1
            vil -= self.power
            print(f'{self.name} сражается {days} день(дня)..., осталось {vil} воинов.\n')
            sleep(1)
        print(f'\n{self.name} одержал победу спустя {days} дней(дня)!')



# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')