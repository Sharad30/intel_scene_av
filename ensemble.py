import pandas as pd
import glob
from functools import reduce

def ensemble():

    path = r'ensemble_submissions/' # use your path
    all_files = glob.glob(path + "/*.csv")

    li = []
    for filename in all_files:
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)

    df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['image_name'], how='inner'), li)
    df_merged.set_index('image_name', inplace=True)
    df_merged = df_merged.mode(axis='columns', numeric_only=True)
    submission_df = df_merged.drop(columns=[1]).astype(int).rename(columns={0:'label'})

    return submission_df

if __name__=='__main__':
    submission_df = ensemble()