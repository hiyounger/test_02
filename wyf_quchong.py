#encoding:utf-8
import pandas as pd
import config
def need_01():
    csv_info= pd.read_csv(config.url,usecols=[1])
    csv_list=csv_info["姓名"]
    csv_list=list(csv_list)
    csv_set=set(csv_list)
    return len(csv_set)


