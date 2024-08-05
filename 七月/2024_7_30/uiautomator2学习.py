import uiautomator2 as u2
# 连接并启动
d = u2.connect()
print(d.info)

import uiautomator2 as u2

def open_app( app_package_name):
    d.app_start(app_package_name)

app_package_name = "com.android.launcher3"
open_app( app_package_name)