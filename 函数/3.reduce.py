from functools import reduce

def add(x,y):
    return x+y

def to10(x,y):
    return 10*x+y
print(reduce(add,[1,2,3,4,5]))
print(reduce(to10,[1,2,3,4,5]))
#reduce函数对数据两两进行处理