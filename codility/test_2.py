import numpy as np
import pandas as pd


def solution(files):
    # files - any of available files, i.e:
    # files = ["./data/framp.csv", "./data/gnyned.csv", "./data/gwoomed.csv",
    #            "./data/hoilled.csv", "./data/plent.csv", "./data/throwsh.csv",
    #            "./data/twerche.csv", "./data/veeme.csv"]

    # write your solution here

    nested_list = []

    for file in files:

        df = pd.read_csv(file)
        df["date"] = df["date"].astype('datetime64[ns]')
        
        df1 = df.groupby('date', as_index=False)['vol'].sum()
        df1 = df1.set_index(df1['date'].rename('year').dt.year, append=True).swaplevel(0, 1)
        df1 = df1.groupby("year").max()
        df1 = df1.reset_index(drop=True)

        df2 = df.groupby('date', as_index=False)['close'].sum()
        df2 = df2.set_index(df2['date'].rename('year').dt.year, append=True).swaplevel(0, 1)
        df2 = df2.loc[df2.groupby("year")["close"].idxmax()]

        nested_list.append([df1, df2])

    return nested_list


import os
caminho = "D:\Kaio_Poc_Telhas\codility"
files_list = [os.path.join(caminho, filename) for filename in os.listdir(caminho) if filename.endswith(".csv")]
solution(files_list)