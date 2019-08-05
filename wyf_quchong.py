#encoding:utf-8
import pandas as pd
if __name__ == '__main__':

    csv_info= pd.read_csv("E:/test_02_0805/daka.csv",usecols=[1])
    csv_list=csv_info["姓名"]
    csv_list=list(csv_list)
    csv_set=set(csv_list)
    print(csv_set)
    print(len(csv_set))


