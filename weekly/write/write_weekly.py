import pandas as pd
import xlwt
import os

def write_weekly(save_path,weekly_name,df):
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    df.to_excel(save_path+weekly_name)

