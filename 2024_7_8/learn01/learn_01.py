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


