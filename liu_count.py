#encoding:utf-8
import csv
import config
def need_02():
    with open(config.url, 'r', encoding="utf-8") as mycsvfile:
        data = list(csv.reader(mycsvfile))
        data.pop(0)
    dic = {}
    for i in range(len(data)):
        if data[i][10] != "未打卡":
            if data[i][1] not in dic:
                dic[data[i][1]] = 1
            else:
                dic[data[i][1]] += 1
    for a, b in dic.items():
        print (a, "打卡", b, "次")