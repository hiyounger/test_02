# encoding:utf-8
import config
import csv


def way(reader):
    count=0
    list=[]
    for i in range(len(list)):
        pass
if __name__ == '__main__':
    reader = list(csv.reader(open(config.url, encoding="utf-8")))
    print(type(reader))
    for re in reader:
        print(re[1], re[10])

#     将数据加到列表中：
