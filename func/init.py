# 测试网络
from func.networkisok import network_test

if not network_test():
    print("[ERROR] 网络不通！请检查您的网络是否正常！")
    print("[INFO]  进程退出异常，代码-2，网络连接故障。如果您需要离线运行，请参阅离线安装教程：https://blog.geekgame.top/")
    exit(-2)
