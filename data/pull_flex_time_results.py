import pandas as pd
import os
# from app import cache
# from mods.DBA import s3_connect
# from mods.DBA import S3_folderpaths



def load_funnel():
    curr_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(curr_path, 'funnel_data.csv')   
    
    data_types = {'stage_int_sort': str, 'YYYYMM': str}
    df_funnel = pd.read_csv(path, dtype=data_types)
    
    return df_funnel

def load_medium_funnel():
    curr_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(curr_path, 'medium_funnel_data.csv')   
    
    data_types = {'stage_int_sort': str, 'YYYYMM': str}
    df_medium_funnel = pd.read_csv(path, dtype=data_types)
    
    return df_medium_funnel
