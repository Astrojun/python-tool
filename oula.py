#任何大于2的偶数都能表示为两个质数之和

import math

def is_primenum(num):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                return False
        return True
    else:
        return False

def is_evennum(num):
    if (num % 2) == 0:
        return True
    return False

def cal_sum(num):
    success = 0
    for i in range(2, math.ceil(num/2) + 1):
        if is_primenum(i) and is_primenum(num - i):
            print('%d = %d + %d' % (num, i, num - i))
            success+=1
    if success == 0:
        print('求和失败')

while(True):
    num = int(input())
    if (num > 2) and is_evennum(num):
        cal_sum(num)
    else:
        print('请输入大于2的偶数')
