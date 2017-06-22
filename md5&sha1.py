#计算文件MD5和SHA1值

import hashlib
import os,sys

def CalcHexSha1(filepath):
    with open(filepath,'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.hexdigest()
        return hash

def CalcHexMD5(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
        return hash

def CalcSha1(filepath):
    with open(filepath,'rb') as f:
        sha1obj = hashlib.sha1()
        sha1obj.update(f.read())
        hash = sha1obj.digest()
        return hash

def CalcMD5(filepath):
    with open(filepath,'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.digest()
        return hash

if __name__ == "__main__":
    filepath = input()
    if os.path.exists(hashfile):
        print(CalcHexMD5(filepath))
        print(CalcHexSha1(filepath))
