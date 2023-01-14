from time import sleep

from func import init
from func.operate import *

with open("res/json/main.json", 'r') as load_f:
    load_dict = json.load(load_f)
author = load_dict['Author']
version = load_dict['Version']
print('''
JMCL-Server-CLI是由某畜种牲（没错！就是%s本大人！）开发的一款为了方便小白管理服务器的CLI工具！
版本：%s
操作：'''
      % (author, version))
sleep(0.1)
init.network_test_main()
init_opt()
