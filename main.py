import json

with open("res/json/main.json", 'r') as load_f:
    load_dict = json.load(load_f)
author = load_dict['Author']
version = load_dict['Version']
print('''
欢迎使用%s开发的JMCL-Server-CLI!
版本：%s
操作：
''' % (author, version))
