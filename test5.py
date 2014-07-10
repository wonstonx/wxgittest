__author__ = 'wangxun'

nums=range(10,10000)
print [n for n in nums if n==sum((int(i)**4 for i in str(n)))]

