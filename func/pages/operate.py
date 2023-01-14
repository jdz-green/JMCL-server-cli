# -!- coding: utf-8 -!-
import json

from func.pages.download_server_core import start_download

with open("res/json/operations.json", 'r', encoding='utf-8') as load_f:
    load_dict = json.load(load_f)


def operate(num):
    op_description = load_dict["ops"][str(num)]
    if op_description == "download_server_core":
        start_download()


def init_opt():
    opt = load_dict["series"]
    for i in range(len(opt)):
        print("[ %s ]" % opt[i] + ' ' + load_dict["description"][str(opt[i])])
    opt_num = input("输入指定数字以进行相应操作：")
    operate(opt_num)


if __name__ == '__main__':
    init_opt()
