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