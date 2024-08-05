from datetime import datetime
def log(func):
    def warpper(*a,**b):
        start_time = datetime.now()
        start_time = (f'开始被调用时间：{start_time.strftime("%Y-%m-%d %H:%M:%S")}')
        print(start_time)
        res = func(*a,**b)
        end_time = datetime.now()
        end_time = (f'结束被调用时间：{end_time.strftime("%Y-%m-%d %H:%M:%S")}')
        print(end_time)
        return res
    return warpper

@log
def hello():
    print('你好啊')
hello()