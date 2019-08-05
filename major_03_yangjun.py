# encoding:utf-8
import csv
import config
import pandas
from datetime import datetime


# 将用户名去重,得到所有的用户列表
def get_username():
    csv_info = pandas.read_csv(config.url, usecols=[1])
    csv_list = csv_info["姓名"]
    csv_list = list(csv_list)
    csv_set = set(csv_list)
    user_list = list(csv_set)
    user_new_list = []
    first_time = 0
    last_time = 0
    count = 0
    week = 1
    for user in user_list:
        user_new_list.append([user, first_time, last_time, 0, count, week])
    # print(user_new_list)
    return user_new_list


# 获得所有的用户名和用户时间
def get_userNameAndTime():
    reader = list(csv.reader(open(config.url, encoding='utf-8')))
    list_nameAndTime = []
    i = 0
    for re in reader:
        if i == 0:
            i = 1
            continue
        list_nameAndTime.append([re[0], re[1]])
    return list_nameAndTime


def need_03(user_list, list_time):
    for i in range(len(list_time)):
        for j in range(len(user_list)):
            if list_time[i][1] == user_list[j][0] and user_list[j][3] == 0:
                user_list[j][1] = list_time[i][0]
                user_list[j][3] = 1
            if list_time[i][1] == user_list[j][0]:
                user_list[j][2] = list_time[i][0]
    return user_list


def get_need_03(list_time_new):
    for i in range(len(list_time_new)):
        date_first = datetime.strptime(list_time_new[i][1], "%Y/%m/%d")
        date_last = datetime.strptime(list_time_new[i][2], "%Y/%m/%d")
        days = date_last - date_first
        day = days.days
        list_time_new[i][3] += day
        week = datetime.strptime(list_time_new[i][1], "%Y/%m/%d").weekday()
        list_time_new[i][5] += week
    return list_time_new


def get_count_daka(list_new):
    for i in range(len(list_new)):
        x = int(list_new[i][3] // 7)
        x1 = int(list_new[i][3] / 7)
        if x != x1:
            x = x + 1
            list_new[i][4] = x * 6 + list_new[i][4]
    for i in range(len(list_new)):
        j = int(list_new[i][3] % 7)
        if j + list_new[i][5] <= 6:
            list_new[i][4] = j * 2 + list_new[i][4]
        else:
            list_new[i][4] = (j - 1) * 2 + list_new[i][4]
    print(list_new)
    return list_new


if __name__ == '__main__':
    user = get_username()
    # print(get_username())
    time = get_userNameAndTime()
    # print(get_userNameAndTime())
    # print(need_03(user,time))
    time1 = need_03(user, time)
    # print(get_need_03(time1))
    time1 = get_need_03(time1)
    time2 = get_need_03(time1)
    print(time2)
    for i in range(len(time2)):
        print("%s 应该打卡 %s 次" % (time2[i][0], time2[i][3] - 1))
