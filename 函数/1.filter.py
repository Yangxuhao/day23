

func=(lambda  x:x%2==1)
print(func(1))
print(func(2))


def isit(x):
    return x%2==1
mylist=list(filter(isit,[1,2,3,4,5,6,7]))
print(mylist)