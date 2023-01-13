import urllib3


def network_test():
    try:
        http = urllib3.PoolManager()
        http.request('GET', 'https://baidu.com')
        return True
    except Exception as e:
        return False

# print(network_test())
