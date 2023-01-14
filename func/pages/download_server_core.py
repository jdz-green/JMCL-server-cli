# -!- coding: utf-8 -!-
import gc
import json

# def version(url,version):
#     begin=url.find('[')
#     end=url.find(']')
from func.check_java import check_for_java
from func.threaddownload import single_thread_download


def start_download():
    with open("res/json/cores.json", 'r', encoding='utf-8') as load_f:
        load_dict = json.load(load_f)
    iter_name = 1
    for i in load_dict["cores"]:
        print("[ %a ] %s" % (iter_name, load_dict["description"][i]))
        iter_name += 1
    gc.collect()
    num = int(input('请选择核心：')) - 1
    name = load_dict["cores"][num]
    i = 1
    versions_list = load_dict[load_dict["cores"][num]]
    for item in versions_list:
        print("[ %a ] %s" % (i, item))
        i += 1
    num = int(input("请选择版本："))
    print(versions_list[num - 1])
    single_thread_download(load_dict["urls"][name] + str(versions_list[num - 1]) + "/server",
                           "downloads/%s.jar" % hash(versions_list[num - 1]))
    check_for_java();
