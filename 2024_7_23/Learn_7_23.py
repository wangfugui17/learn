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
dict_a = {"a":'123',1:'abc',"c":456,a:213456978}
print(dict_a)




