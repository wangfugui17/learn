
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