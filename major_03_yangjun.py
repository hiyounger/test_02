# encoding=utf-8

import csv
import pandas
import config
import time
# 将用户名去重,得到所有的用户列表
def get_username():
    csv_info= pandas.read_csv(config.url,usecols=[1])
    csv_list=csv_info["姓名"]
    csv_list=list(csv_list)
    csv_set=set(csv_list)
    user_list=list(csv_set)
    user_new_list=[]
    count=0
    for user in user_list:
        user_new_list.append([user,count])
    # print(user_new_list)
    return user_new_list

def need_03(list1):
    reader=list(csv.reader(open(config.url,encoding="utf-8")))
    list_user=list1
    for i in range(len(reader)):
        for j in range(len(list_user)):
            if reader[i][1]==list_user[j][0]:
                list_user[j][1]+=1
                continue
    for us in list_user:
        print("%s 需要打卡的次数是：%s" % (us[0], us[1]))

# date = 0
# name = 1

# with open("D:/kaoqin.csv/kaoqin.csv","r",encoding="utf-8") as csvfile:
#     user = list(csv.reader(csvfile))
#
#     # print(user)
#
#     dic={}
#     for i in range(1,len(user)):
#         if user[i][1] not in dic:
#             dic[user[i][1]] = user[i][0]
#     print(dic)
#
#     # for a,b in dic.items():
#     #     print(a,"\t",b,"\t")










