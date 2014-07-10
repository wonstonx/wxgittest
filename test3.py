__author__ = 'wangxun'

def cal(min, max,mi):
    for i in range(min,max):
        a=0
        for n in str(i):
            a+=int(n)**mi
        if i==a:
            print i


