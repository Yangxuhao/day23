import csv
import operator

path=r"C:\Users\xuhao_yang\PycharmProjects\day23\000001.csv"

reader=csv.reader(open(path,"r"))
alllist=[]
for item in reader:
    # print(item)
    alllist.append(item)

alllist.sort(key=operator.itemgetter(3))
alllist.reverse()
for line in alllist:
    print(line)