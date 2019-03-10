import urllib
import urllib.request
import threading

def getstock(i):
    url="http://hq.sinajs.cn/list=sz300"+str(i)
    print(urllib.request.urlopen(url).read().decode("gbk"),end="")

threadlist=[]
sam=threading.Semaphore(10)
for i in range(100,150):
    with sam:
        th=threading.Thread(target=getstock,args=(i,))
        th.start()
        threadlist.append(th)

for thd in threadlist:
    thd.join()