import pandas as pd
import xlwt

def read_weekly(excel_group_path):
    df_list=[]
    for excel in excel_group_path:
        df = pd.read_excel(excel,error_bad_lines=False)
        df_list.append(df)
        df.info()
    return df_list