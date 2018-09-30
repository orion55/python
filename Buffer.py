import functools


class Buffer:
    # конструктор без аргументов
    def __init__(self):
        self.list = []

    # добавить следующую часть последовательности
    def add(self, *a):
        for i in a:
            self.list.append(i)
            if len(self.list) == 5:
                print(functools.reduce(lambda a, x: a + x, self.list, 0))
                self.list.clear()

    # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
    # добавлены
    def get_current_part(self):
        return self.list


buf = Buffer()
print(buf.add(1, 2, 3))
print(buf.get_current_part())  # вернуть [1, 2, 3]
print(buf.add(4, 5, 6))  # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part())  # вернуть [6]
print(buf.add(7, 8, 9, 10))  # print(40) – вывод суммы второй пятерки элементов
print(buf.get_current_part())  # вернуть []
print(buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
print(buf.get_current_part())  # вернуть [1]
