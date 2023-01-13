# 这是一个示例 Python 脚本。
import ssl

import wget

from func.hash import *
from func.threaddownload import mydownload, singledownload

ssl._create_default_https_context = ssl._create_unverified_context

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    version=input("请输入版本号：")
    print(myhash(version))
    # wget.download('https://bmclapi2.bangbang93.com/version/'+version+"/server", myhash(version)+'.jar')
    singledownload("https://bmclapi2.bangbang93.com/version/"+str(version)+"/server", myhash(version) + '.jar')
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

def version(version):
    print('将保存为'+myhash(version)+'.jar')
    singledownload("https://bmclapi2.bangbang93.com/version/" + str(version) + "/server", '../tmp/'+myhash(version) + '.jar')