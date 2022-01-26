class MoneyBox:
    count = 0

    def __init__(self, capacity):  # конструктор с аргументом – вместимость копилки
        self.capacity = capacity

    def can_add(self, v):  # True, если можно добавить v монет, False иначе
        return True if self.count + v <= self.capacity else False

    def add(self, v):  # положить v монет в копилку
        if self.can_add(v):
            self.count += v


class Buffer:
    list_of_numbers = []

    def __init__(self):
        pass

    def add(self, *a):
        for i in a:
            self.list_of_numbers.append(i)
        while len(self.list_of_numbers) >= 5:
            sum_of_five = 0
            for i in range(5):
                sum_of_five += self.list_of_numbers[i]
            del self.list_of_numbers[0:5]
            print(sum_of_five)

    def get_current_part(self):
        return self.list_of_numbers


# buf = Buffer()
# buf.add(1, 2, 3)
# buf.get_current_part() # вернуть [1, 2, 3]
# buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
# buf.get_current_part() # вернуть [6]
# buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
# buf.get_current_part() # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# buf.get_current_part() # вернуть [1]
class A:
   def foo(self):
      print("A")

class B(A):
   pass

class C(A):
   def foo(self):
      print("C")

class D:
   def foo(self):
      print("D")

class E(B, C, D):
   pass

E().foo()