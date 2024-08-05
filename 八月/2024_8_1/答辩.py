str_01 = '  Abcde_123456789   saeer  '
str_02 = '123184984'
str_03 = 'https://www.abcdee.com.cn'
str_upper = str_01.upper()
print(str_upper)
str_lower = str_01.lower()
print(str_lower)
print(str_01.title())

print(f"{str_01}说：你好{str_02}")
print("{:-^50s}".format("分割线"))

print(f'这是"\\n":{str_01} \n {str_02} "表现为换行"')
print(f'这是"\\t":{str_01} \t {str_02} "表现为长空白"')

print("{:-^50s}".format("分割线"))
print(f'{str_01.lstrip()}移除左端的空白')
print(f'{str_01.rstrip()}移除右端的空白')
print(f'{str_01.strip()}移除两端的空白')

print("{:-^50s}".format("分割线"))
str_03 =str_03.removeprefix('https://')
print(f'删除前缀：{str_03}')

print('a'*50)



print("{:-^50s}".format("分割线"))
print(f'整数和浮点数')
num_01 = 12
num_02 = num_01**2
num_03 = num_01/2
num_04 = num_01//2
print(f'乘方：{num_02}',type(num_02))
print(f'除{num_03}',type(num_03))
print(f'整除{num_04}',type(num_04))


print("{:-^50s}".format("列表"))

list_01 = ['a','b','c','d']
print(list_01)
print(list_01[0])
print(list_01[-1])
print(f'小{list_01[0].upper()}是一个好人')

print("{:-^50s}".format("添加列表"))
list_01.append('e')
list_01.insert(2,'f')
print(list_01)

print("{:-^50s}".format("删除列表"))

del list_01[0]
print(list_01)

list_01.pop(0)
print(list_01)
print('被删除的是：'+list_01.pop(0))
print(list_01)

list_01 = ['a','b','c','d','r']
list_01.remove('a')
print(list_01)

list_02 =[4,2,1,3,8,4,2,6]
print("排序后" , sorted(list_02))
print(list_02)
list_02.sort()
print(list_02)
list_02.sort(reverse=True)
print(list_02)
list_03 = [2,5,814,41,156,'a']
list_03.reverse()
print(list_03)
print(len(list_03))


print("{:-^50s}".format("操作列表"))

def caozuoliebiao():
    list_04 = ['a',123,456,'你好',45]
    for list_05 in list_04:
        print(list_05)
    return list_04
# caozuoliebiao()
# print(caozuoliebiao())


# pop_list = [1,23,2]
# abc_list = pop_list
# print(abc_list)

# 力扣
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。
# 更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
# 返回 k
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         k = 0
#         for num in nums.copy():
#             if num == val:
#                 nums.remove(num)
#             else:
#                 k += 1


list_06 = []
for i in range(0,12):
    list_06.append(i ** 2)
print(list_06)

list_07 = [i ** 2 for i in range(0,9)]
print(list_07)

print(max(list_07))
print(min(list_07))
print(sum(list_07))

print(list_07[1:3])
print(list_07[1:])
print(list_07[-2:])



print("{:-^50s}".format("分割线"))
players = ['charles', 'martina', 'michael', 'florence']
for player in players:
    print(player.title())


print("{:-^50s}".format("分割线"))
def up_cars():
    cars = ['audi', 'bmw', 'subaru', 'toyota']
    for car in cars:
        if car == 'bmw':
            print(car.upper())
        else:
            print(car.title())
up_cars()


car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')


print("{:-^50s}".format("分割线"))
list_09 = [1,2,3,'a','m']
print('a' in list_09)
print('b' in list_09)
print('a' not in list_09)

list_09 = [];
if list_09:
    print('非空')
else:
    print('空')


print("{:-^50s}".format("字典"))
dictionary_01 = {'color':'green','age':18,'num':5}
print(dictionary_01['color'])
print(dictionary_01['age'])

del dictionary_01['color']
print(dictionary_01)

value_01 = dictionary_01.get('color')
print(value_01)
value_01 = dictionary_01.get('age')
print(value_01)

favorites = {'jen': 'python', 'edward': 'rust'}
for name, language in favorites.items():
    print(f"{name} loves {language}.")

for name in favorites.keys():
    language =favorites[name].title()
    print(f"{name} loves {language}.")


for language in favorites.values():
    print(language.title())

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0,alien_1,alien_2]

name_01 = input('请输入名字')
print(name_01)

# 7.23
import math

counter = 100
miles =1000.0
name = "John"

# 二进制转换
print('二进制转十进制:', int('1010', 2))
print('十进制转二进制:', bin(10))
print('十进制转二进制并去掉前缀:', bin(10)[2:])
print("{:-^50s}".format("分割线"))

print('对应的Ascll的数值',ord('v'))
print(float("-inf"))
# inf为无穷大 -inf为无穷小

a = b = c = 1
a,b,c = 1,2,'abcd'
print(a,b,c)

# all() 函数用于判断可迭代对象（如列表、元组、字符串等）中的所有元素是否都为真值
# （除了 0、空字符串、空列表等被视为假值的元素外，其他都视为真值）。
# 如果所有元素都为真值，all() 函数返回 True；否则，返回 False 。
c = [0,1,2,'flase']
if all(c):
    print('为Ture')
else:
    print('为flase')

b = 2.4
c = 2.8
print('向上取整',math.ceil(b))
print('向下取整',math.floor(b))
print('向零取整',math.floor(b))
print('四舍五入',"'1.1':",round(b),'"1.9":',round(c))


print("{:-^50s}".format("list"))
list_a = [123,'abc']
print(list_a[0])
print(list_a[1:3])
print(list_a[2:])

list_b = [ i**2 for i in range(0,5)]
print(list_b)
list_b =[ i+1 for i in range(3,9)]
print(list_b)
list_b =[ i/1 for i in range(1,10,2)]
print(list_b)

print("{:=^50s}".format('分割线'))
n,m =4,5
dp = [[1]*n ] +[[1]+[0]*(n-1) for _ in range(m-1)]
print(dp)
# ????????????????????????????????
# clone_node.neighbors =[self.cloneGraph(n)for n in node.neighbors
print(list_b*2)
list_b.append('abcd')
print(list_b)
del list_b[-1]
print(list_b)
print('删除的元素是：',list_b.pop(3))
# pop和def的区别，pop会返回被删除的元素
list_b.append(list_a)#引用传递
print('list_b为：',list_b)
list_b.append([]+list_a)#值传递
print('list_b:',list_a)


# ???????????
# list_b.append(list_b(path))
print("{:=^50s}".format('分割线'))

print(len([1,2,3]))
list_a = [1,2,3] + [4,5,6]
print(list_a)
list_a = ['a']* 5
print(list_a)
flag_a =3 in [1,2,3]#判断3是否在列表中
print(flag_a)
for x in list_a:print(x,1,2,3)
# print(list_a)
list_a = [i for i in range(1,5)]
print(list_a)
print(list_a[::-1])#数组反转
print(max(list_a))

# 求和
print(sum((1,2,3,4)))
print(sum(list_a))
print(sum(list_a[i] for i in range(len(list_a))))
list_a = (1 in s for s in list_a)
print(list_a)

list_a = [12, 21, 34, 51]
new_list = [str(1) in str(s) for s in list_a]
# 对于 list_a 中的每个元素 s，将其转换为字符串，
# 然后检查字符串 '1' 是否在转换后的字符串中，将结果依次放入 new_list 中
print(new_list)

list_a.sort()
print(list_a)
list_a.sort(reverse=True)#倒叙
print(list_a)

print("{:=^50s}".format('分割线'))
# ???????
# list_a.sort(a,key = len,reversed=True)
# print(list_a)
print(list_a)
# ????????????????????????????????????????????????
# def f(item):
#     return item[1]
# list_a.sort(key= f)
# print(list_a)


words = ["apple", "babbbbbbbbbbbbbbbbbbbbbbnana", "cherry", "date"]
res = sorted(words, key=lambda word: -len(word))
print(res)


print([(x,y,z) for x in [1,2] for y in [3,4,] for z in [5,6]])



print("{:=^50s}".format('元组'))
# : 是分隔符，用于分隔字段名和格式规范。
# = 表示填充字符为 = 。
# ^ 表示居中对齐。
# 50 表示总宽度为 50 个字符。
# s 表示要格式化的对象是字符串。
# format('分割线') 表示将字符串 '分割线' 按照前面指定的格式进行格式化。
tuple_a = (123,'abc')

print("{:=^50s}".format('字典'))
dict_a = {"a":'123',1:'abc',"c":456,c:213456978}
print(dict_a)

print(dict_a.values())
print(list(dict_a.values()))

for key in dict_a:
    print(f'{key}:{dict_a[key]}')

print(dict_a.keys())
dict_b = {'a':1,'b':2,'c':3}
max_dict_a = max(dict_b.values())
print('最大的值：',max_dict_a)

dict_b['a'] = 100
print(dict_b)
dict_b['age'] = 50
print(dict_b)
del dict_b['age']
print(dict_b)
dict_b.clear()
print(dict_b)
del dict_b#删除字典


print(dict_a.get('a',0))
print(dict_a)


import re




try:
    with open('../2024_7_24/身份证信息.csv', 'r', encoding='utf-8') as file:
        try:
            with open('../2024_7_24/身份证日期信息.txt', 'a', encoding='utf-8') as f:
                for line in file:
                    f.write(''.join(re.findall('(19\d{2}-\d{2}-[0123]\d|20\d{2}-\d{2}-[0123]\d) ', line)))
        except IOError as e:
            print('写入',e)
except FileNotFoundError as e:
    print(e)

import re

# Time_list =[]
# with open('身份证信息.csv', 'r',encoding='utf-8') as file:
#     for line in file:
#         Time_list.append(re.findall('[12][09]\d{2}-\d{2}-[0123]\d',line))
#
#
#
# with open('身份证日期信息.txt','w',encoding='utf-8') as f:#清空上一次
#     f.close()
#
#
# with open('身份证日期信息.txt','w',encoding='utf-8') as f:
#     for i in range(len(Time_list)):
#         f.write("".join(Time_list[i]))
#         f.write('\n')
#     f.close()









# 关键
with open('身份证信息.csv','r',encoding='utf-8') as file:
    # with open('身份证日期信息.txt','w',encoding='utf-8') as fi:
    #     fi.close()
    #追加模式下，可通过打开关闭清空掉文件内容
    with open('身份证日期信息.txt','w',encoding='utf-8') as f:#a+设置追加模式
        for line in file:
            f.write(''.join(re.findall('(19\d{2}-\d{2}-[0123]\d|20\d{2}-\d{2}-[0123]\d)',line))+'\n')



# import re
#
# try:
#     # 读文件错误
#     with open('身份证信息.csv', 'r', encoding='utf-8') as file:
#         with
#         open('身份证日期信息.txt', 'a+', encoding='utf-8') as f:
#             for line in file:
#                 #写文件错误
#                 try:
#                     f.write(''.join(re.findall('[12][09]\d{2}-\d{2}-[0123]\d', line)))
#                     f.write('\n')
#                 except Exception as e:
#                     print(f"写文件时发生错误: {e}")
#             print('写入成功')
# except FileNotFoundError as e:
#     print(f"文件未找到或无法访问{e}")
# except IOError as e:
#     print(f"输入输出错误: {e}")
# except Exception as e:
#     print(f"错误: {e}")





# import re
# # gbk
# try:
#     try:
#         #  gbk
#         with open('身份证信息.csv', 'r', encoding='gbk') as file:
#             with open('身份证日期信息.txt', 'a+', encoding='utf-8') as f:
#                 for line in file:
#                     try:
#                         f.write(''.join(re.findall('[12][09]\d{2}-\d{2}-[0123]\d', line)))
#                         f.write('\n')
#                     except Exception as e:
#                         print(f"写文件时发生错误: {e}")
#             print('写入成功')
#     except UnicodeDecodeError:
#         # utf8
#         with open('身份证信息.csv', 'r', encoding='utf-8') as file:
#             with open('身份证日期信息.txt', 'a+', encoding='utf-8') as f:
#                 for line in file:
#                     try:
#                         f.write(''.join(re.findall('[12][09]\d{2}-\d{2}-[0123]\d', line)))
#                         f.write('\n')
#                     except Exception as e:
#                         print(f"写文件时发生错误: {e}")
#             print('写入成功')
# except FileNotFoundError as e:
#     print(f"文件未找到或无法访问{e}")
# except Exception as e:
#     print(f"错误: {e}")



dict_a = {'a':1,'b':2,3:'c'}
print(dict_a['a'])
print('{:=^50s}'.format('分割线'))

print(dict_a.values())
print(list(dict_a.values()))
for key in dict_a:
    print(key)
print('{:*^50s}'.format('分割线'))
dict_b = {'a':1,'b':2,'c':3,'d':4}
dict_c = max(dict_b.values())
print(dict_c)
dict_b['a']=100
dict_b['s']=11000000000000
print(dict_b)
del dict_b['a']
print(dict_b)
dict_b.clear()
print(dict_b)
print('{:*^50s}'.format('分割线'))
dict_b = {'a':1,'b':2,'c':3,'d':4}
print(dict_b.get('c',0))
print(dict_b.items())
print(dict_b)


dict_b = {'a': 10, 'b': 20, 'c': 30, 'd': 20}  # 定义一个名为 dict_b 的字典
new_list = [key for key,value in dict_b.items() if value==20]  # 使用列表推导式创建一个新的列表。对于字典 dict_b 中的每一个键值对 (key, c)，如果值 c 等于 20，则将键 key 放入新列表 new_list 中
print(new_list)  # 打印新创建的列表


# dict_b = {'a': 10, 'b': 20, 'c': 30, 'd': 20}
# new_list = [dict_b[key] for key in dict_b if key == 'a']
# print(new_list)


parame = {1,2,3,4,'a','b','c'}
parame_a  = set([1,2,3,54])
print(parame_a)

parame_a.add('aaaaaaaaaaaaaaaaaa')
print(parame_a)
parame_a.update(dict_b)
print(parame_a)
parame_a.remove(1)#移除指定的元素,不存在则会报错
print(parame_a)
# parame_a.discard()#移除指定的元素,不存在（不会）报错
print('{:*^50s}'.format('分割线'))
parame_a.clear()#清空集合
print(parame_a)
# x in s

for key in parame:
    print(key)





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




class Student:
    school_name = '小明'
    def __init__(self,name,age,hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
        # print(f'{self.name}的年龄是{self.age}，他的兴趣爱好是{self.hobby}')

    def chinese(self):
        print(self.name+'说你好')
    def english(self):
        print(self.name+'说 hello')

abc_1 = Student('小花',18,'踢足球')
# abc_1.school_name = '小红'
abc_1.chinese()
abc_1.english()
print(f'{abc_1.name}的年龄是{abc_1.age}，他的兴趣爱好是{abc_1.hobby}')


class Father:
    money = 99999
    house = '大平层'
class Son_1(Father):
    pass
son_obj =Son_1()
print(son_obj.house)


class People:
    school = '清华大学'
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
class Teacher(People):
    def __init__(self,name,sex,age,title):
        super().__init__(name,age,sex)
        self.title = title
        def teach(self):
            print(f'{self.name}是老师')
obj = Teacher('lili','female',28,'高级教师')
print(obj.__dict__)
print(People.__dict__)


class MyClass:
    school_name = '老年人大学'
    __age = 18

    def __choice_course(self):
        print('李华正在选课')
obj = MyClass()


# words = [ 'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'aroun'
# 'd', 'the', 'eyes', 'look', 'into', 'my', 'eyes', "you're", 'under' ]
#
# num = 0
# for i in range(len(words)):
#     for j in range(1,len(words)):
#         if words[i] == words[j]:
#             num += 1
#             words.pop(words[j])
#     print(f'{words[i]}:{num}')
#     num = 0

res = 1
def jiecheng (n):
    res = 1
    for i in range(1,n+1):
        res = res * (i+1)
        i += 1
    return res
jiecheng(100)
print(res)

# sum = 0
# for i in range(1,101):
#     sum += i
# print(sum)

# sum = 0
# n = 0
# while n<101 :
#     n += 1
#     sum += i
# print(sum)

nums = [1,3,5,7,9]
max = nums[0]
min = nums[0]
avg = 0
sum = 0
for i in range(len(nums)):
    if max < nums[i]:
        max = nums[i]
    if min > nums[i]:
        min = nums[i]
    sum += nums[i]
avg = sum / len(nums)
print(max,min,avg)

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min = 0
max = 0
sum = 0
avg = 0
n = 0
for values in prices.values():
    if max < values:
        max = values
    if min > values:
        min = values
    sum += values
    n += 1
avg = sum / n
print(max,min,avg)


nums = [1,4,-5,10,-7,'N/A',3,-1]
n = 1
new_list = []
for num in nums:
    if type(n) == type(num):
        if num < 0:
            new_list.append(num)
print(new_list)



words = [ 'look', 'into','my', 'eyes', 'look', 'into','my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into','my', 'eyes', "you're", 'under' ]

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f'{word}: {count}')




#是否可以以字符串名的形式导入模块？如果可以，如何操作？请使用代码示例

# 可通过importlib模块
import importlib

module_name = "math"
module = importlib.import_module(module_name)

print(module.pi)

# 使用while循环计算1到100的和
# 哈哈写错字了
sum = 0
n = 0
while n<101 :
    n += 1
    sum += n
print(sum)


# 如何构造一个可接受任意数量的函数？请用代码展示（包含位置参数，和关键字参数）
def my_function(*args, **kwargs):
    print("位置参数：", args)
    print("关键字参数：", kwargs)

my_function(1, 2, 3, name="张三", age=20)


# 创建一个类的实例，可不可以绕过类的 __init__()方法？如果可以如何实现？
# 用__new__实际上，他才是真正的构建函数
class MyClass:
    def __new__(cls, *args, **kwargs):
        instance = super(MyClass, cls).__new__(cls)
        # 在这里可以进行一些自定义的操作
        return instance

my_instance = MyClass()


# 编写一个对象，让其支持上下文管理协议（with语句）
# 重点是__enter__和__exit__
class MyContextManager:
    def __enter__(self):
        print("进入上下文")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("退出上下文")

with MyContextManager() as obj:
    print("在上下文中执行操作")

    words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes',
             'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes',
             "you're", 'under']

# 编写代码找出以下words序列中出现频率最高的3个单词（写出解题思路得2分）
    # 解题思路：
    # 1. 使用字典来统计每个单词出现的次数。
    # 2. 对字典按照值（即单词出现的次数）进行排序。
    # 3. 取出排序后的前 3 个单词及其出现的次数。
words = [ 'look', 'into','my', 'eyes', 'look', 'into','my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into','my', 'eyes', "you're", 'under' ]

# 解题思路：
# 1. 使用字典来统计每个单词出现的次数。
# 2. 对字典按照值（即单词出现的次数）进行排序。
# 3. 取出排序后的前 3 个单词及其出现的次数。

word_count = {}  # 创建一个空字典用于存储单词及其出现的次数

for word in words:  # 遍历单词列表
    if word in word_count:  # 如果单词已经在字典中，次数加 1
        word_count[word] += 1
    else:  # 如果单词不在字典中，初始化为 1
        word_count[word] = 1

sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)  # 按照单词出现次数降序排序

top_3_words = sorted_word_count[:3]  # 取出前 3 个

for word, count in top_3_words:  # 打印前 3 个单词及其出现次数
    print(f"{word}: {count}")


# 编写代码，使用递归计算100的阶乘[n! = 1 x 2 x 3 x ... x 100]
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(100))



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
        pass
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




# =====================================================================================

import pandas as pd
from IPython.display import display,clear_output,Markdown
import os
from coze import Coze
import uiautomator2 as u2
import time

os.environ['COZE_API_TOKEN'] = 'pat_ESCxaeS8auGTdt3GG1CwCMJgkgTTJoVEqCh048coFSjjUjkKNTPsPo0zfnA8NdtK'
os.environ['COZE_BOT_ID'] = "7397332462814494760"

chat = Coze(api_token= os.environ['COZE_API_TOKEN'],
            bot_id = os.environ['COZE_BOT_ID'],
            max_chat_rounds=10,
            stream=False)

d = u2.connect()


fu_jiedian = d(resourceId="com.tencent.mm:id/bp0").child(resourceId='com.tencent.mm:id/bn1')
path = d(resourceId="com.tencent.mm:id/bkl")
new_message = ''
flag = False

def panduan():
    global path
    global flag
    while flag == False:
        if path[-1].right(className='android.widget.RelativeLayout') is None:
            flag = True
            print(flag)
        time.sleep(1)
    print(flag)

def chat_ai_auto(*a,**b):
    global flag
    global new_message
    panduan()
    for i in range(len(fu_jiedian)):
        print(i)
        print(len(fu_jiedian))
        new_message = path[i].get_text()

    if flag:  # 判断是不是自己发出去的
        botAi = chat(new_message)
        d.xpath('//android.widget.EditText').set_text('')
        d.xpath('//android.widget.EditText').set_text(f'{botAi}')
        send_input = d(resourceId="com.tencent.mm:id/bql")
        send_input.click()
        flag = False

    else:
        print('对方还没有回复')

chat_ai_auto()
    # return chat_ai_auto()
def xiaoxiye():
    message_list = d(resourceId="com.tencent.mm:id/j8g").child(resourceId = 'com.tencent.mm:id/cj1')
    message_num = message_list.child(resourceId = 'com.tencent.mm:id/o_u')

    if new_message_text() > 0:

        for i in range(1,len(message_list)):
            if d(resourceId="com.tencent.mm:id/cj0")[i].child(className="android.widget.RelativeLayout").child(resourceId='com.tencent.mm:id/o_u') is not None:
                message_list[i].child(resourceId='com.tencent.mm:id/a_4').click()
                chat_ai_auto()
                d(description='返回').click()
                print('找到消息了')
            else:
                print('暂时没找到新消息')

xiaoxiye()


def new_message_text():
    message_fu_addr = d(resourceId="com.tencent.mm:id/cj0")[0].child(className="android.widget.RelativeLayout").child(resourceId='com.tencent.mm:id/o_u')
    while len(message_fu_addr) <= 0:
        print('收到新消息了！')
    return len(message_fu_addr)
new_message_text()


