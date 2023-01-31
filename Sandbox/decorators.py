'''
@lru_cache
Caches the result of a function so that subsequent calls to the 
function with the same arguments will not be executed again.
'''
import time


def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


start_time = time.perf_counter()
print(fibonacci(30))
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")
# The execution time: 0.18129450 seconds

from functools import lru_cache
import time


@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


start_time = time.perf_counter()
print(fibonacci(30))
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")
# The execution time: 0.00002990 seconds

'''
The @total_ordering decorator from the functools module is used to generate 
the missing comparison methods for a Python class based on the ones that are defined.
We save a bit on writing all the ge, gt, and le dunder methods.
'''
from functools import total_ordering


@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade


student1 = Student("Alice", 85)
student2 = Student("Bob", 75)
student3 = Student("Charlie", 85)

print(student1 < student2)  # False
print(student1 > student2)  # True
print(student1 == student3)  # True
print(student1 <= student3) # True
print(student3 >= student2) # True

'''
Sometimes, we need to define a customized context manager for some 
special requirements. In this case, the @contextmanager decorator is our friend.
'''

from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    print("The file is opening...")
    file = open(filename,mode)
    yield file
    print("The file is closing...")
    file.close()

with file_manager('test.txt', 'w') as f:
    f.write('Yang is writing!')
# The file is opening...
# The file is closing...

'''
Different OOP languages have different mechanisms to define getters and setters. 
In Python, we can simply use the @property decorator.
'''
class Student:
    def __init__(self):
        self._score = 0

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, s):
        if 0 <= s <= 100:
            self._score = s
        else:
            raise ValueError('The score must be between 0 ~ 100!')

Yang = Student()

Yang.score=99
print(Yang.score)
# 99

Yang.score = 999
# ValueError: The score must be between 0 ~ 100!

'''
@cached_property It can transform a method of a class into a property whose 
value is computed once and then cached as a normal attribute for the life of the instance.
'''

from functools import cached_property

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @cached_property
    def area(self):
        return 3.14 * self.radius ** 2


circle = Circle(10)
print(circle.area)
# prints 314.0
print(circle.area)
# returns the cached result (314.0) directly

'''
Instance methods: methods that are bound to an instance. 
They can access and modify the instance data. An instance method is called on an instance of the class, and it can access the instance data through the self parameter.

Class methods: methods that are bound to the class. They can’t modify the instance data. 
A class method is called on the class itself, and it receives the class as the first parameter, which is conventionally named cls.

Static methods: methods that are not bound to the instance or the class.
The instance methods can be defined as normal Python functions as long as its first parameter is self. However, to define a class method, we need to use the @classmethod decorator.
'''

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def from_diameter(cls, diameter):
        return cls(diameter / 2)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2


c = Circle.from_diameter(8)
print(c.radius)  # 4.0
print(c.diameter)  # 8.0

'''
To define a static method, we just need to use the @staticmethod decorator.
'''
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = None

    def set_nickname(self, name):
        self.nickname = name

    @staticmethod
    def suitable_age(age):
        return 6 <= age <= 70


print(Student.suitable_age(99)) # False
print(Student.suitable_age(27)) # True
print(Student('yang', 'zhou').suitable_age(27)) # True

'''
The @dataclass decorator (introduced in Python 3.7) can automatically generate 
several special methods for a class, such as __init__, __repr__, __eq__, __lt__, and so on.
'''
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

point = Point(1.0, 2.0)
print(point)
# Point(x=1.0, y=2.0)

'''
The @register decorator from the atexit module can allow us to execute a function when the Python interpreter is exiting.
'''
import atexit

@atexit.register
def goodbye():
    print("Bye bye!")

print("Hello Yang!")

# Hello Yang!
# Bye bye!