# 测试网络
from func.networkisok import *


def network_test_main():
    if not network_test_dl():
        if not network_test():
            print("[ERROR] 网络不通！请检查您的网络是否正常！")
            print("[INFO]  进程退出异常，代码-2，网络连接故障。如果您需要离线运行，请参阅离线安装教程：https://blog.geekgame.top/")
            exit(-2)
        else:
            print("[HAHA]  啊哦(〃'▽'〃)！————服务器好像睡觉了呢！不用担心，没有中心服务器也照样玩！不过不能更新了呢。。。")
            return
    if network_test_dl6():
        print("好耶！您的网络支持IPv6线路！速度直接起飞！")
        with open('res/ipv6_status.dat', 'w') as f:
            f.write("1")  # 文件的写操作
    else:
        with open('res/ipv6_status.dat', 'w') as f:
            f.write("0")  # 文件的写操作
    return
