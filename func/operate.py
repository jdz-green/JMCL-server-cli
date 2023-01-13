# -!- coding: utf-8 -!-
import json

with open("../res/operations.json", 'r', encoding='utf-8') as load_f:
    load_dict = json.load(load_f)


def init():
    print("输入指定数字以进行相应操作：")
    opt = load_dict["ops"]
    for i in range(len(opt)):
        print("[ %s ]" % opt[i] + ' ' + load_dict["description"][str(opt[i])])


if __name__ == '__main__':
    init()
