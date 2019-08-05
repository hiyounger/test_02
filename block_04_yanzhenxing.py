# encoding:utf-8
import config
import csv
import pandas

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
# 将用户名存储到字典中，方便统计正常打卡次数
# def get_dict(user_list):
#     user_dict={}
#     count=0
#     for user in user_list:
#         user_new=user
#         user_dict[user_new]=count
#     return user_dict
def need_way_04(user_list):
    reader = list(csv.reader(open(config.url, encoding="utf-8")))
    list_user = get_username()
    for i in range(len(reader)):
        for j in range(len(list_user)):
            if reader[i][1] == list_user[j][0] and reader[i][10] == "正常":
                list_user[j][1] += 1
    for us in list_user:
        print("%s 正常打卡的次数是：%s" % (us[0], us[1]))
    # print(user_list)
    # reader = list(csv.reader(open(config.url, encoding="utf-8")))
    # print(type(reader))
    # # 将第一个用户加入到用户字典中
    # user=reader[1][1]
    # count=0
    # dict_user={user:count}
    # for re in reader:
    #     pass
        # 判断用户是否在表中
        # tmp=0
        # for i in range(len(user_list)):
        #     if re[1][1]==user_list[i]:
        #         tmp=1
        #     if tmp==1:
        #         continue
        # if tmp==1:
        #     for


#     将数据加到列表中：
