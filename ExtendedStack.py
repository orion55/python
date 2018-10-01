class ExtendedStack(list):
    # операция сложения
    def sum(self):
        self.append(self.pop() + self.pop())

    # операция вычитания
    def sub(self):
        self.append(self.pop() - self.pop())

    # операция умножения
    def mul(self):
        self.append(self.pop() * self.pop())

    # операция целочисленного деления
    def div(self):
        self.append(self.pop() // self.pop())


ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
ex_stack.div()
ex_stack.pop()  # == 2
ex_stack.sub()
ex_stack.pop()  # == 6
ex_stack.sum()
ex_stack.pop()  # == 7
ex_stack.mul()
ex_stack.pop()  # == 2
len(ex_stack)  # == 0
