from audioop import avg

p = (4,5)
x,y = p
print(x,y)
# 任何的序列（或者是可迭代对象）可以通过一个简单的赋值语句解压并赋值给多
# 个变量。唯一的前提就是变量的数量必须跟序列元素的数量是一样的
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
name, shares, price, date = data
print(name, shares, price, date)

s = 'hello'
a,b,c,d,e = s
print(a,b,c,d,e)

def drop_first_last(gardes):
    first, *middle,last = gardes
    print(middle)
    return sum(middle)/len(middle)
print(drop_first_last((1,99,99,99,99,99,99,1)))


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(name,phone_numbers)
def duibi(month):
    *first_seven,eight = month
    return sum(first_seven)/len(first_seven),eight
print(duibi((1,2,3,4,5,6,7,8)))


def sum(items):
    head, *tail = items
    return head + sum(tail) if tail else head
print(sum((1,2,3,4,5,6,7,8,9)))

import heapq
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))


prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price,':::::::::::',max_price)

price_sorted = sorted(zip(prices.values(),prices.keys()))
print(price_sorted)


a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}
b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}
print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())

c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)


words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
'my', 'eyes', "you're", 'under'
]

words_nums = {}
for word in words:
    if word in words_nums:
        words_nums[word] +=1
    else:
        words_nums[word] = 1
word_sorted = sorted(words_nums.items(),key=lambda x:x[1],reverse=True)
print(word_sorted)
for key,value in word_sorted:
    print(f'{key}:{value}')


mylist = [1, 4, -5, 10, -7, 2, 3, -1]
mylist_1 = [value for value in mylist if value >2]
print(mylist_1)


prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}

# p1 = {key:value for key,value in price.items() if value > 200 }

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)



def ppower(x):
    return x*x
def power(x,n):
    s = 1
    while n>0:
        n -= 1
        s = s*x
    return s


def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum+n*n
        return sum
nums = [1,2,3]
calc(*nums)

def person(name,age,**kw):
    print('name:', name, 'age:', age, 'other:', kw)
abc ={'aaa':13,'bbb':14}
person('aa',30,city='北京',**abc)

def person(name,age,*,city,job):
    print(name,age,city,job)

def person(name,age,*arges,city,job):
    print(name,age,arges,city,job)

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

def mul(x, y=1,*z):
    chengji = 1
    for i in z:
        chengji = i*chengji
    return x * y*chengji

# 测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')





class Logout:
    def __init__(self):
        self.logs = []
    def createlog(self,**message):

import datetime
import time

class LogOutput:
    def __init__(self):
        self.logs = []

    def log(self, message):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{current_time}] {message}"
        print(log_message)
        self.logs.append(log_message)

    def save_logs(self):
        with open("log.txt", "w") as file:
            for log in self.logs:
                file.write(log + "\n")

# 示例用法
if __name__ == "__main__":
    log_output = LogOutput()

    log_output.log("这是第一条日志")
    time.sleep(2)
    log_output.log("这是第二条日志")
    log_output.save_logs()



