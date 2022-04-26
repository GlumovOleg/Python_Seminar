# Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

from time import * #time
# from time import sleep


def time_random():
    return time() - int(str(time()).split('.')[0])

def gen_random_range(start, stop):
    return int(time_random() * (start - stop) + stop)

for i in range(12):
    print (gen_random_range(10,40), end=' ')
    sleep(0.1)

# seconds = 1575721830.711298
# local_time = time.time(seconds)
# print("Местное время:", local_time)