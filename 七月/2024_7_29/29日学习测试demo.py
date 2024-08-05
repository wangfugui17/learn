# 你需要将一个字符串分割为多个字段，但是分隔符 (还有周围的空格) 并不是固定
# 的。
str_abc = 'asdadas dagvfsdgf; hsahnfids, jniaksnj,joidajs, adsada'
import re
new_list = re.split(r'[;,\s]\s*',str_abc)
print(new_list)

# 当你使用 re.split() 函数时候，需要特别注意的是正则表达式中是否包含一个括
# # 号捕获分组。如果使用了捕获分组，那么被匹配的文本也将出现在结果列表中。比如，
# # 观察一下这段代码运行后的结果

# 如:r'(;|,|\s)\s*'

# [;,\s]\s* 的含义是
# ：匹配分号 ; 、逗号 , 或者空白字符（包括空格、制表符、换行符等）\s
# ，并且后面可能跟着零个或多个空白字符 \s*

new_list_1 = re.split(r'(;|,|\s)\s*',str_abc)
print(new_list_1)

new_list_2 = new_list_1[1::2]
# new_list_2 = new_list_1[::2]
print(new_list_2)
# startswith() 或者 endswith()匹配开头或结尾
# 如果你想检查多种匹配可能，只需要将所有的匹配项放入到一个元组中去，然后传
# 给 startswith() 或者 endswith() 方法：
# 这个方法中必须要输入一个元组作为参数
# 要确保传递参数前先调用 tuple() 将其转换为元组类型
wangzhi = 'www.abc.com'
new_wangzhi = wangzhi.endswith('.com')
print(new_wangzhi)
import os
filenames = os.listdir('.')
print(filenames)
new_list_3 = [name for name in filenames if name.endswith(('a','y'))]
print(new_list_3)



text = 'yeah, but no, but yeah, but no, but yeah'

print(text.startswith('yeah'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')


dict_num = {}
newlist = []
with open('happy.txt','r',encoding = 'gbk') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split(' ')
        for word in line:
            if word in dict_num:
                dict_num[word] += 1
            else:
                dict_num[word] = 1
sorted_word_count = sorted(dict_num.items(), key=lambda x: x[1], reverse=True)  # 按照单词出现次数降序排序

top_words = sorted_word_count[:10]
print(top_words)



def digui(n):
    if n == 1 or n==0:
        return 1
    else:
        return n + digui(n-1)
print(digui(100))


def digui_1(n):
    if n/10 <1:
        return n
    else:
        return (n%10) + digui_1(int(n/10))
print(digui_1(12345))


dict_abc = {}
with open('A.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        line = re.split(r'[,;\n]',line)
        line = [word for word in line if re.match(r'\S',word)]
        for word in line :
            if word in dict_abc:
                dict_abc[word] += 1
            else:
                dict_abc[word] = 1

sorted_word = sorted(dict_abc.items(), key=lambda x: x[1], reverse=True)
with open('B.txt', 'w+', encoding='utf-8') as file:
    for item in sorted_word:
        file.write(str(item[0]) + ':' + str(item[1]) + '\n')  # 增加换行符，使输出更清晰
        print(item)


zidian_1 = {}
import random
for i in range(26):
    zidian_1[chr(97+i)] = int((random.random()*100)+1)
print(zidian_1)

zidian_paixu = stord