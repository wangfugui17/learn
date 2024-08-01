# coding: utf-8
#
import pandas as pd
from IPython.display import display,clear_output,Markdown
import os
from coze import Coze
os.environ['COZE_API_TOKEN'] = 'pat_ESCxaeS8auGTdt3GG1CwCMJgkgTTJoVEqCh048coFSjjUjkKNTPsPo0zfnA8NdtK'
os.environ['COZE_BOT_ID'] = "7397332462814494760"




chat = Coze(api_token= os.environ['COZE_API_TOKEN'],
            bot_id = os.environ['COZE_BOT_ID'],
            max_chat_rounds=10,
            stream=False)



# 获取当前前台应用的包名
import uiautomator2 as u2
d = u2.connect()
# 获取当前前台应用信息
current_app = d.app_current()

# 尝试查找具有文本 "微信" 的元素
wechat_element = d(text="微信")

# 如果找到了，说明应用未打开，启动应用
if  wechat_element.exists:
    package_name = "com.tencent.mm"  # 假设微信的包名是这个
    d.app_start(package_name)

# 找到所有类名为 android.widget.RelativeLayout 的元素
# relative_layout_elements = d(className="android.widget.RelativeLayout")
#
# for layout in relative_layout_elements:
#     # 遍历 RelativeLayout 的子元素
#     children = layout.child().child(resourceId = 'com.tencent.mm:id/o4k').child(className = '''android.widget.LinearLayout
# ''').child()
#     print(children.get_text())
#     for child in children:
#         if child.get_text() == 'DROP TABLE user_name':
#             # 尝试获取 id 为 com.tencent.mm:id/ht5 的子元素的 text
#             target_child = layout.child(resourceId="com.tencent.mm:id/ht5")
#             if target_child.exists:
#                 print(target_child.get_text())


# yemian = d(text = 'DROP TABLE user_name').down(className = 'android.view.View').get_text()
# print(yemian)
# user_message ={}
#
# childen = list(d(className ='android.widget.LinearLayout'))
# print(childen.get_text())
# for child in childen:
#     if child.child(resourceId='com.tencent.mm:id/o_u').get_text() is not None:
#         user_name = d(resourceId='com.tencent.mm:id/o_u').right(className='android.view.View').get_text()
#         user_message[user_name] = d(resourceId='com.tencent.mm:id/o_u').get_text()
#         print(user_name)
#         print(user_message)
#     else:
#         print('没有新消息')


import uiautomator2 as u2
import time

d = u2.connect()

fu_jiedian = d(resourceId="com.tencent.mm:id/bp0").child(resourceId='com.tencent.mm:id/bn1')
new_message = ''
path = d(resourceId="com.tencent.mm:id/bkl")
flag = False
def panduan():
    if path[-1].right(className='android.widget.RelativeLayout') is None:
        flag = True

def chat_ai_auto():
    panduan()
    for i in range(len(fu_jiedian)):
        new_message = path[i].get_text()

    if flag:  # 判断是不是自己发出去的
        botAi = chat(new_message)
        # 在这里延迟10秒执行
        # time.sleep(10)
        d.xpath('//android.widget.EditText').set_text('')
        input_text = d.xpath('//android.widget.EditText').set_text(f'{botAi}')
        send_input = d(resourceId="com.tencent.mm:id/bql")
        send_input.click()
    else:
        print('对方还没有回复')

    print(f'这是最新的信息:{new_message}')
chat_ai_auto()


