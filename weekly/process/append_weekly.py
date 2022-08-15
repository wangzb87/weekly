import pandas as pd
import xlwt

def append_weekly(dframes):
    result_df = pd.concat(dframes)
    return result_df

# frames = [df1, df2, df3]
# result = pd.concat(frames)