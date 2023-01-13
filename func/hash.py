import hashlib


def myhash(version):
    md5 = hashlib.md5(b'Mikufans')
    md5.update(version.encode('utf-8'))
    name = md5.hexdigest()
    # print(type(name))
    return name

# print(myhash('1.19.1'))