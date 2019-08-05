# encoding:utf-8
import config
import csv

# 将用户名去重
def way(reader):
    list=set(reader)
    print(type(list))
    return list
if __name__ == '__main__':
    reader = list(csv.reader(open(config.url, encoding="utf-8")))
    print(type(reader))
    for re in reader:
        print(re[1], re[10])

#     将数据加到列表中：
