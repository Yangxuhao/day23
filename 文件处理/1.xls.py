from collections import OrderedDict
from pyexcel_xls import get_data
from pyexcel_xls import save_data

def readxls():
    path=r"C:\Users\xuhao_yang\PycharmProjects\day23\1.xls"
    xlsdata=get_data(path)
    #print(xlsdata)
    for sheet in xlsdata:
        print(sheet,":",xlsdata[sheet])

def writexls():
    path="myself.xls"
    data=OrderedDict()
    sheet_1=[]
    row1=["a","b","c"]
    row2=[1,2,3]
    sheet_1.append(row1)
    sheet_1.append(row2)

    data.update({"abc":sheet_1})
    save_data(path,data)

writexls()
# readxls()