from random import randint
import time

#рекурсивный подход
def recurs(listic, number, up, down ):
    if down > up:
        return None
    middle = (up + down) // 2
    if listic[middle] == number:
        return middle
    if listic[middle] > number:
        return recurs(listic, number, middle - 1, down)
    if listic[middle] < number:
        return recurs(listic, number, up, middle + 1)

#итеративный подход
def iter(listic, number, up, down):
    while down <= up:
        middle = (up + down) // 2
        if listic[middle] > number:
            up = middle - 1
        elif listic[middle] < number:
            down = middle + 1
        else:
            return middle
    return None


listic = []
for i in range(100):
    listic.append(randint(-100, 100))
listic.sort()
number = int(input('Введите число в диапазоне (-100, 100), идекс которого хотите найти: '))
up = len(listic) - 1
down = 0

def main_1():
    start = time.time()
    print(recurs(listic, number, up, down))
    print('Время работы рекурсивного метода: ' + str(time.time() - start) + ' сек.')

def main_2():
    start = time.time()
    print(iter(listic, number, up, down))
    print('Время работы итеративного метода: ' + str(time.time() - start) + ' сек.')

main_1()
main_2()