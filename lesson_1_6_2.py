class ExtendedStack(list):
    def sum(self):  # операция сложения
        if len(self) >= 2:
            a = self.pop()
            b = self.pop()
            sum = a + b
            self.append(sum)
        else:
            return False

    def sub(self):  # операция вычитания
        if len(self) >= 2:
            a = self.pop()
            b = self.pop()
            sub = a - b
            self.append(sub)
        else:
            return False

    def mul(self):  # операция умножения
        if len(self) >= 2:
            a = self.pop()
            b = self.pop()
            mul = a * b
            self.append(mul)
        else:
            return False

    def div(self):  # операция целочисленного деления
        if len(self) >= 2:
            a = self.pop()
            b = self.pop()
            div = a // b
            self.append(div)
        else:
            return False
