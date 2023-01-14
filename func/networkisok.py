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
        http.request('GET', 'https://dl.geekgame.top')
        return True
    except Exception as e:
        return False

# print(network_test())
