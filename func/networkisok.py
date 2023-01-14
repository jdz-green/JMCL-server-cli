# -!- coding: utf-8 -!-
import subprocess

import urllib3


def network_test():
    try:
        http = urllib3.PoolManager()
        http.request('GET', 'https://baidu.com')
        return True
    except Exception as e:
        return False


def network_test_dl():
    try:
        http = urllib3.PoolManager()
        http.request('GET', 'https://dl.geekgame.top/index.html')
        return True
    except Exception as e:
        return False


def network_test_dl6():
    # http = urllib3.PoolManager()
    # http.request('GET', 'https://dl6.geekgame.top/index.html')

    ret = subprocess.run("ping dl6.geekgame.top -n 1", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return True if ret.returncode == 0 else False

# print(network_test())
