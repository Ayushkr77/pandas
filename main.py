import pandas as pd

# print(pd.__version__)



# Series: A Series is a one-dimensional labeled array that can hold data of any type. Think of it like a single column in a spreadsheet.
# Each value in a Series has an associated index label (like row numbers, but can be customized).

data=[101,102,103]
series=pd.Series(data)
# print(data)
# print(type(series))
print(series)   # at the end meta data will also be printed

series1=pd.Series(data, index=["a","b","c"])   # in index, we can pass a list, tuple, dictionary, numpy array, or even another series
print(series1)
print(series1.loc["a"])   # .loc is a label-based indexer. It is used to access elements in a Series (or rows/columns in a DataFrame) by their labels (not positions).

series1.loc["c"]=200
print(series1)

# now .iloc-> position based selection.
print(series1.iloc[0])
series1.iloc[2]=103
print(series1)


data1=[90,101,97,200,205]
series2=pd.Series(data1, index=["a","b","c","d","e"])
series3=series2[series2<100]
print(series3)
print(series2[series2>100])



calories={"Day 1":1500, "Day 2":1800, "Day 3":2100}
series4=pd.Series(calories)    # dont provide index as we have passed dictionary
print(series4)
print(series4.loc["Day 1"])
series4.iloc[1]+=500
print(series4)
print(series4[series4>2000])



# --------------------------------------------------------------------------------------------



