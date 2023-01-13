# 这是一个示例 Python 脚本。
import ssl

from func.hash import *
from func.threaddownload import *

ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.76'
}


def request_jd(url):
    response = requests.get(url=url, headers=headers)
    # return response.headers.get('location')
    return response.headers  # .get('location')


def version(version):
    print('将保存为' + myhash(version) + '.jar')
    single_thread_download("https://bmclapi2.bangbang93.com/version/" + str(version) + "/server",
                           '../tmp/' + myhash(version) + '.jar')


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    versions = input("请输入版本号：")
    # print(request_jd("https://bmclapi2.bangbang93.com/version/1.7.10/server"))
    print(myhash(versions))
    # wget.download('https://bmclapi2.bangbang93.com/version/'+version+"/server", myhash(version)+'.jar')
    # singledownload("https://bmclapi2.bangbang93.com/version/"+str(version)+"/server", myhash(version) + '.jar')
    # 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
    version(versions)
