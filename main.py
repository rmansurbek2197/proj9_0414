# 41. Filter ishlatish
lst = list(map(int, input().split()))
print(list(filter(lambda x: x % 2 == 0, lst)))

# 42. Reduce ishlatish
from functools import reduce
lst = list(map(int, input().split()))
print(reduce(lambda a, b: a+b, lst))

# 43. Klass yaratish
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Ali")
print(p.name)

# 44. Meros olish
class Student(Person):
    pass

s = Student("Vali")
print(s.name)

# 45. Modul yaratish (misol)
def greet():
    print("Salom")
