#Source Code:
import pandas as pd
def sortcsv(file,column,top_num):
    data = pd.read_csv(file)
    out = data.sort_values(column,axis=0,ascending=False,inplace=False)
    out = out.drop_duplicates("Country")
    outtop = out.head(top_num)
    outtop.to_csv("Top" + " " + str(top_num) + " " + column + ".csv")