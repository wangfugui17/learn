import functools
from types import MethodType

int2 = functools.partial(int,base=2)
print(int2('1000000'))

class Student(object):
    pass
Student.name = '李四'
s =Student()
s.name = '张三'
print(s.name)
print(Student.name)

def set_age(self,age):
    self.age = age
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

s2 = Student()

def set_score(self,score):
    self.score = score
Student.set_score = set_score

s2.set_score(50)
print(s2.score)


class Student2():
    __slots__ = ('name', 'age')

s3 = Student2()
s3.name = '王五'
# s3.score = 100
print(s3.name)
# print(s3.score)


class  Student():
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
s4 = Student()
s4.set_score(60)
# s4.set_score(600)


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s5 = Student()
s5.score = 50
s5.score
print(s5.score)



class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2024 - self._birth
s6 =Student()
s6.birth = 2003
print(s6.birth)
print(s6.age)


class Screen(object):
    __slots__ = ('_width','_height','_resolution')
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,a):
        self._width = a
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,a):
        self._height = a
    @property
    def resolution(self):
        return self._height * self._width

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')



def a (abc):
    def warpper(*a,**b):
        print('空函数执行前======')
        res = abc(*a,**b)
        print('空函数执行后=======')
        return res
    return warpper

@a
def 空函数():
    print('空函数正在执行++++++++++')
空函数()




class Animal(object):
    pass
class Mammal(Animal):
    pass
class Runnable(object):
    def run(self):
        print('跑着呢')

class Flyable(object):
    def run(self):
        print('飞着呢')
class Bird(Animal):
    pass
class Dog(Mammal,Runnable):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass
dog = Dog()
dog.run()


class Fib(object):
    def __init__(self):
        self.a,self.b =0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f = Fib()
print(f[0])

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
s = Student('张三')
s()