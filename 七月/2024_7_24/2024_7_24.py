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