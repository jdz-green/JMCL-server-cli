import os
import re


def check_for_java():
    print("正在检测Java环境……", end="")
    p = os.popen('java -version 2>&1').read()
    version = re.findall(r'"(.+?)"', p)[0]
    print("Java版本： %s" % version)
   