__author__ = 'wangxun'

def cal(filename):

#    name=[i.strip() for i in open(filename)]
#    name.sort()
#    return(sum((sum((ord(a)-64) for a in i))*(index+1) for index, i in enumerate(name)))


    names=[i.strip() for i in open(filename)]
    names=sorted(names)
    f=lambda x,y:sum([ord(word)-64 for word in x]) *y
    values=[f(name,index+1) for index, name in enumerate(names)]

    return(sum(values))

print cal("names1.txt")
