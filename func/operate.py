# -!- coding: utf-8 -!-
import json

with open("res/json/operations.json", 'r', encoding='utf-8') as load_f:
    load_dict = json.load(load_f)


def operate(num):
    print(num)


def init_opt():
    opt = load_dict["series"]
    for i in range(len(opt)):
        print("[ %s ]" % opt[i] + ' ' + load_dict["description"][str(opt[i])])
    opt_num = input("输入指定数字以进行相应操作：")
    operate(opt_num)


if __name__ == '__main__':
    init_opt()
