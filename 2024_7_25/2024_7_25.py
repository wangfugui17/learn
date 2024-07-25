import math

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]
print(L[0][0])
print(L[1][1])
print(L[-1][-1])

# birth = input('birth:')
# if birth :
#     print('有值')
# else:
#     print('无值')



def bim_count(Xiaoming_lenght,Xiaoming_weith):
    BMI_Xiaoming = Xiaoming_weith / Xiaoming_lenght ** 2
    if BMI_Xiaoming > 32:
        print('严重肥胖')
    elif BMI_Xiaoming > 28:
        print('肥胖')
    elif BMI_Xiaoming > 25:
        print('过重')
    elif BMI_Xiaoming > 18.5:
        print('正常')
    else:
        print('过轻')
    print(BMI_Xiaoming)
bim_count(1.75,80)


def AAA(age):
    match age:
        case x if age < 10:
            print(f'{x} years old')
        case 10:
            print('10 years old.')
        case 11|12|13|14|15|16|17|18:
            print('11~18 years old')
        case 19:
            print('19 years old')
        case _:
            print('not sure')
AAA(8)

args = ['gcc', 'hello.c', 'world.c']
# args = ['clean']
# args = ['gcc']

match args:
    # 如果仅出现gcc，报错:
    case ['gcc']:
        print('gcc: missing source file(s).')
    # 出现gcc，且至少指定了一个文件:
    case ['gcc', file1, *files]:
        print('gcc compile: ' + file1 + ', ' + ', '.join(files))
    # 仅出现clean:
    case ['clean']:
        print('clean')
    case _:
        print('invalid command.')
# 第一个case ['gcc']表示列表仅有'gcc'一个字符串，没有指定文件名，报错；
#
# 第二个case ['gcc', file1, *files]表示列表第一个字符串是'gcc'，第二个字符串绑定到变量file1，后面的任意个字符串绑定到*files（符号*的作用将在函数的参数中讲解），它实际上表示至少指定一个文件；
#
# 第三个case ['clean']表示列表仅有'clean'一个字符串；
#
# 最后一个case _表示其他所有情况。


names = ['Michael','BOb','TRACY']
for name in names:
    print(name)
sum = 0
for x in [1,2,3,4,5,6,7,8,9]:
    sum += x
print(sum)


sum = 0
n = 0
while n<101:
    sum += n
    n+=1
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for l in L:
    print(f'Hello {l}')


sum = 0
n = 0
while n<101:
    sum += n
    n += 1
    if sum >2000 :
        break
print(sum)
# continue跳过当前循环,开始下一次循环
# 提前结束循环,break
sum = 0
n = 0
while n <101:#满足条件才执行
    n += 1
    if sum > 2000:
        continue
    sum += n
print(sum)


d = {'A':12,'B':13}
if 'c' in d:
    print(d['c'])
else:
    print('c''不存在')

print(d.get('B'))
print(d.pop('A'))
print(d)

s = set([1, 2, 3])
print(s)
# 重复元素在set中自动被过滤：
# add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
# 通过remove(key)方法可以删除元素：

n1 = 255
n2 = hex(n1)
print(n2)


def quadratic(a=None, b=None, c=None):
    x1 = (-1*b) + math.sqrt(b**2-4*a*c)/(2*a)
    x2 = (-1*b) - math.sqrt(b**2-4*a*c)/(2*a)
    return x1,x2
print('x::::::::::::::::',quadratic(1,-5,6))
print('{:+^50s}'.format('分割线'))



# 汉诺塔移动，把n个盘将a移到c，途中经转b
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)  #根部迭代，一次情况下，直接 a --> c 移动
        return
    move(n-1, a, c, b)              #把a中的n-1个盘移动到b，途中经转c
    print('move', a, '-->', c)      #把a中的1个盘移动到c
    move(n-1, b, a, c)              #把b中的n-1个盘移动到c，途中经转a

move(4, 'A', 'B', 'C')



L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])



# 测试:
# if trim('hello  ') != 'hello':
#     print('1测试失败!')
# elif trim('  hello') != 'hello':
#     print('2测试失败!')
# elif trim('  hello  ') != 'hello':
#     print('3测试失败!')
# elif trim('  hello  world  ') != 'hello  world':
#     print('4测试失败!')
# elif trim('') != '':
#     print('5测试失败!')
# elif trim('    ') != '':
#     print('6测试失败!')
# else:
#     print('7测试成功!')


d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for valus in d.values():
    print(valus)
for k,y in d.items():
    print(k,y)

def findMinAndMax(L):
    if not L:  # 如果列表为空
        return (None, None)
    maxNum = L[0]
    minNum = L[0]
    for x in L:
        if x > maxNum:
            maxNum = x
        if x < minNum:
            minNum = x
    return (minNum, maxNum)

if findMinAndMax([]) != (None, None):
    print('1测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('2测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('3测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('4测试失败!')
else:
    print('5测试成功!')

list_a = [x**2 for x in range(1,11) if x%2 == 0]
print(list_a)
list_a = [f'{n}+{m}' for n in range(1,10) for m in range(1,10)]
print(list_a)

import  os
list_a = [d for d in os.listdir('.')]
print(list_a)
print(os.listdir())

d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k,v in d.items():
    print(k,'=',v)

list_a = [k+'='+v for k,v in d.items()]
print(list_a)

L = ['Hello', 'World', 'IBM', 'Apple']
L_a = [i.lower() for i in L]
print(L_a)

list_a = [x if x%2==0 else -x for x in range(1,11)]
print(list_a)


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = odd()
next(o)
next(o)
next(o)


def triangles():
    row = [1]
    yield row
    while True:
        next_row = [1]
        for i in range(1, len(row)):
            next_row.append(row[i - 1] + row[i])
        next_row.append(1)
        row = next_row
        yield row
n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')


