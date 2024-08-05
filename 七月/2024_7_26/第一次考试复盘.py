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