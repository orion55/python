class MoneyBox:

    # конструктор с аргументом – вместимость копилки
    def __init__(self, capacity=0):
        self.capacity = capacity
        self.count = 0

    # True, если можно добавить v монет, False иначе
    def can_add(self, v):
        return self.count + v <= self.capacity

    # положить v монет в копилку
    def add(self, v):
        if self.can_add(v):
            self.count += v
            return self.count


x = MoneyBox(15)
print(x.add(5))
print(x.add(9))
print(x.add(3))
