class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def __print_score(self):
        print('%s: %s' % (self.__name, self.__score))


    def get_name(self):
        return self.__name
    def set_score(self,score):
        self.__score =score
        return self.__score

abc = Student('zahngsan',123)
print(abc.set_score(93))
print(abc._Student__name)

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender = gender

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')
class Animal():
    def run(self):
        print('Animal is running...')
class dog(Animal):
    def run(self):
        print('dog is running...')
class cat(Animal):
    def run(self):
        print('cat is running...')


abcd = cat()
abcd.run()


class abcedf():
    def run(self):
        print('abcedf is running slowly...')
print(isinstance(abcedf,cat))
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(abcedf())
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')
run_twice(Tortoise())
print(isinstance(abcedf,Animal))


print(dir(abcd))
class Student():
    name = 'student'
    def __init__(self,name):
        self.name = name
s = Student('Bob')
s.score = 90
s.name = 'abcd'
print(s.score)
print(s.name)


class Student():
    count = 0
    def __init__(self,name):
        self.name = name
        self.count_add()

    def count_add(self):
        Student.count +=1

# 测试:
if Student.count != 0:
    print('1测试失败!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('2测试失败!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('3测试失败!')
        else:
            print('Students:', Student.count)
            print('测试通过!')

class Student(object):
    pass
s = Student()
s.name = 'Michael'
print(s.name)


def set_age(self,age):
    self.age =age
from types import MethodType
s.set_age = MethodType(set_age, s)
print(s.set_age(25),s.age)

def set_score(self, score):
    self.score = score

Student.set_score = set_score
s1 = Student()
s2 = Student()
s1.set_score(99)
s2.set_score(100)
print(s1.score)
print(s2.score)

class Student():
    __slots__ = ('name','age')
    # pass
s3 = Student()
# s3.num = 100
s3.age = 10000
print(s3.age)

class Student():
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


def f(x):
    return x*x
r = map(f,[1,2,3,4,5,6,7,8,9])

# print(list(r))
for i in r:
    print(i,'1111111111')



def f(x):
    return x*x
new_list = map(f,[1,2,3,4,5,6,7,8,9])
for i in new_list:
    print(i)





# from datetime import datetime
# class logclass:
#     log_list = []
#     log_count = 0
#     def print_log(self):
#         now = datetime.now()
#         logclass.log_count +=1
#         log_date_format = now.strftime("%Y-%m-%d %H:%M:%S")
#         logclass.log_list.append(f'{log_date_format}\t第{logclass.log_count}次调用')
#         print(log_date_format)
#         print(logclass.log_list)
#     def write_log(self):
#         self.print_log()
#         with open('log.txt','a',encoding ='utf-8') as f:
#             f.write(logclass.log_list[-1]+'\n')
#             print(logclass.log_list[-1])
#
# class b:
#     def method_in_b(self):
#         obj_a = logclass()
#         obj_a.write_log()
#
# bb = b()
# bb.method_in_b()
#
# class c:
#     def method_in_b(self):
#         obj_c =logclass()
#         obj_c.write_log()
# cc = c()
# cc.method_in_b()


print('{:=^50s}'.format('分割线'))
from functools import reduce
def add(x,y):
    return x*10+y
r = reduce(add,[1,3,5,7,9])
print(r)

def int_a(x):
    return int(x)
r = list(map(int_a,'123456798'))
r = reduce(add,r)
print(r,type(r))



def normalize(name):
    return name.capitalize()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def chengji(x,y):
    return x*y
def prod(L):
    return reduce(chengji,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')



from functools import reduce

from functools import reduce

def str2float(s):
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return digits[s]

    def num2int(x, y):
        return x * 10 + y

    s = s.split('.')
    integer_part = reduce(num2int, map(char2num, s[0]))
    decimal_part = reduce(num2int, map(char2num, s[1]))
    return integer_part + decimal_part / (10 ** len(s[1]))

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')


def is_old(n):
    return n%2==1
r = list(filter(is_old,[1,2,3,4,5,6,7,8,9]))
print(r)

def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))


def calc_sum(*arges):
    sum = 0
    for n in arges:
        sum += n
    return sum
print('{:*^50s}'.format('分割线'))
print(calc_sum(1,2,3,4,5,6,7,8,9))

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f())


def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

def inc():
    x = 0
    def fn():
        return x+1
    return  fn
f = inc()
print(f())
print(f())




def createCounter():
    count = 0
    def counter():
        nonlocal count
        count +=1
        return count
    return counter



# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


L = list(filter(lambda n:n%2==0, range(1, 20)))

print(L)

def now():
    print('2024-6-1')
f = now
f()
print(f.__name__)
print(now.__name__)


# def log(func):
#     def wrapper(*args,**kw):
#         print('call %s():' % func.__name__)
#         return func(*args,**kw)
#     return wrapper
#
#
# @log
# def now():
#     print('2024-6-1')
# now()



import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*a,**b):
            print('%s %s():' % (text, func.__name__))
            return func(*a,**b)
        return wrapper
    return decorator

@log('abcdeerd')
def now():
    print('2024-1-1')
now()
print(now.__name__)


def check_arges(func):
    @functools.wraps(func)
    def warpper(*a,**b):
        for i in a:
            if type(i) == int:
                return func(*a, **b)
            else:
                print('请输入整数')

    return warpper


@check_arges
def abcd(*a):
    print('哈哈哈哈哈哈哈哈哈成功执行了')
abcd(1,2,3,4,8)

print('{:*^50s}'.format('分割线'))
def zhaungshuqi(func):
    def warpper(*a,**b):
        print('begin call')
        res = func(*a,**b)
        print('end call')
        return res
    return warpper

@zhaungshuqi
def f():
    print('这就是这个函数')
f()



print('{:*^50s}'.format('这是一条分割线'))
from datetime import datetime
class LogClass:
    log_data = []
    def print_log(func):
        @functools.wraps(func)
        def warpper(self,*a,**b):

            star_time = datetime.now()
            log_date_format = f'{star_time.strftime("%Y-%m-%d %H:%M:%S")}\t开始被{func.__name__}调用'
            LogClass.log_data.append(f'{log_date_format}\n')

            res = func(*a,**b)

            end_time = datetime.now()
            log_date_format = f'{end_time.strftime("%Y-%m-%d %H:%M:%S")}\t结束被{func.__name__}调用'
            LogClass.log_data.append(f'{log_date_format}\n')

            print(LogClass.log_data)
            return res
        return warpper

a = LogClass()
@a.print_log
def print_log():
    print('a')
a.print_log()