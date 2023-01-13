import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests


def calc_divisional_range(filesize, chuck=10):
    step = filesize//chuck
    arr = list(range(0, filesize, step))
    result = []
    for i in range(len(arr)-1):
        s_pos, e_pos = arr[i], arr[i+1]-1
        result.append([s_pos, e_pos])
    result[-1][-1] = filesize-1
    return result


# 下载方法
def range_download(save_name, s_pos, e_pos):
    headers = {"Range": f"bytes={s_pos}-{e_pos}"}
    res = requests.get(url, headers=headers, stream=True)
    with open(save_name, "rb+") as f:
        f.seek(s_pos)
        for chunk in res.iter_content(chunk_size=64*1024):
            if chunk:
                f.write(chunk)


# url = "https://vdn3.vzuu.com/HD/e898cfec-ccf3-11eb-b43a-6ec658071f3e-t1111-vgodrDABRC.mp4?disable_local_cache=1&auth_key=1629707188-0-0-8e6fe4e1e29621664c71e2b95fc3bdb9&f=mp4&bu=http-com&expiration=1629707188&v=tx"
# res = requests.head(url)
# filesize = int(res.headers['Content-Length'])
# divisional_ranges = calc_divisional_range(filesize)

def singledownload(url,save_name):
    with open(save_name, "wb") as f, requests.get(url, stream=True) as res:
        shutil.copyfileobj(res.raw, f)


# save_name = "多线程流式下载.mp4"
# 先创建空文件
def mydownload(url,name):
    res = requests.head(url)
    filesize = int(res.headers['Content-Length'])
    print(filesize)
    divisional_ranges = calc_divisional_range(filesize)
    with open(name, "wb") as f:
        pass
    with ThreadPoolExecutor() as p:
        futures = []
        for s_pos, e_pos in divisional_ranges:
            print(s_pos, e_pos)
            futures.append(p.submit(range_download, name, s_pos, e_pos))
        # 等待所有任务执行完毕
        as_completed(futures)
