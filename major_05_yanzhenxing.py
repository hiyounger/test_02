# encoding:utf-8
import pandas
import config

if __name__ == '__main__':
    print("需求代号")
    print("1：统计考勤表中一共有多少个打卡用户")
    print("2：每个用户打卡多少次")
    print("3：每个用户应该打卡多少次")
    print("4：每个用户正常打卡多少次")
    print("Q:退出程序")
    while 1:
        try:
            print("请输入需求代号")
            need = input("请输入需求代号：例如：1--->")
            if need=="Q":
                break
            if need == str(1):
                print("需求1查询结果：")
                continue
            if need == str(2):
                print("需求2查询结果")
                continue
            if need == str(3):
                print("需求3查询结果")
                continue
            if need == str(4):
                print("需求4查询结果")
                continue
            if need != str(1) and need != str(2):
                if need != str(3) and need != str(4):
                    if need!="Q":
                        print("请输入正确的需求代号：正确的需求代号为：1，2，3，4")
                        continue
        except:
            print('请输入正确的需求代号')
            continue
