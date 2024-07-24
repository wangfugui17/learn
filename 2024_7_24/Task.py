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