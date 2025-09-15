# import pandas as pd

# # print(pd.__version__)



# # Series: A Series is a one-dimensional labeled array that can hold data of any type. Think of it like a single column in a spreadsheet.
# # Each value in a Series has an associated index label (like row numbers, but can be customized).

# data=[101,102,103]
# series=pd.Series(data)   # Series is a constructor, not a function. pd.Series(data) converts Python data structures (list, dict, array, etc.) into a Pandas Series object.       Series is a class inside Pandas. Calling pd.Series(...) means you are calling the constructor of that class to create a new Series object. So yes — it constructs (creates) a Series.
# # print(data)
# # print(type(series))
# print(series)   # at the end meta data will also be printed

# series1=pd.Series(data, index=["a","b","c"])   # in index, we can pass a list, tuple, dictionary, numpy array, or even another series
# print(series1)
# print(series1.loc["a"])   # .loc is a label-based indexer. It is used to access elements in a Series (or rows/columns in a DataFrame) by their labels (not positions).

# series1.loc["c"]=200
# print(series1)

# # now .iloc-> position based selection.
# print(series1.iloc[0])
# series1.iloc[2]=103
# print(series1)


# data1=[90,101,97,200,205]
# series2=pd.Series(data1, index=["a","b","c","d","e"])
# series3=series2[series2<100]
# print(series3)
# print(series2[series2>100])



# calories={"Day 1":1500, "Day 2":1800, "Day 3":2100}
# series4=pd.Series(calories)    # dont provide index as we have passed dictionary
# print(series4)
# print(series4.loc["Day 1"])
# series4.iloc[1]+=500
# print(series4)
# print(series4[series4>2000])



# --------------------------------------------------------------------------------------------



# Dataframe:
# A Pandas DataFrame is a two-dimensional, tabular data structure that works like a spreadsheet with rows and columns.

# import pandas as pd

# data={
#     "Name": ["Spongebob","Squarepants","Patrick"],
#     "Age": [20,30,40]
# }
# print(data)

# df=pd.DataFrame(data)
# print(df)
# df1=pd.DataFrame(data, index=["emp1","emp2","emp3"])
# print(df1)

# print(df1.loc["emp1"])
# print(df.iloc[1])

# # add a new column
# df["Job"]=["Cook","Chef","Cashier"]
# print(df)

# # add a new row
# new_row=pd.DataFrame([{"Name":"Sandy","Age":29,"Job":"Engineer"},
#                       {"Name":"Rahul","Age":25,"Job":"Developer"}])   # see what happens if we write different key like instead of job, try writing something else like role, salary, or anything...
# df=pd.concat([df, new_row])
# print(df)

# new_row1=pd.DataFrame([{"Name":"Sandy","Age":29,"Job":"Engineer"},
#                       {"Name":"Rahul","Age":25,"Job":"Developer"}],
#                       index=["emp4","emp5"])
# df1=pd.concat([df1, new_row1])
# print(df1)


# --------------------------------------------------------------------------------------------

# import pandas as pd

# df=pd.read_csv("data.csv")
# print(df)    # it'll show truncated version, first 5 rows and last 5 rows
# print(df.to_string())     # if want to see full data

# df1=pd.read_json("pokemon.json")
# print(df1)
# print(df1.to_string())   # its still not printing all 150 cols


# --------------------------------------------------------------------------------------------


# Selection in pandas
# Selection in Pandas means pulling out specific data from a Series or DataFrame.

# import pandas as pd

# df=pd.read_csv("data.csv")

# # selection by column
# print(df["Name"])   # can do .to_string()  if want all the cols
# print(df[["Name","Height","Weight"]])

# # selection by rows
# print(df.loc[1])
# # now we'll select rows by using names
# df1=pd.read_csv("data.csv",index_col="Name")
# print(df1)
# print(df1.loc["Pikachu"])

# print(df1.loc["Pikachu",["Height","Weight"]])
# print(df1.loc["Charizard":"Blastoise", ["Height","Weight"]])   # label-based slice on the index. We'll get from Charizard to Blastoise

# print(df1.iloc[0:11])   # will return 11 rows from 0 to 10
# print(df1.iloc[0:11:2])
# print(df1.iloc[0:11:2, 0:3])  # first 3 cols



# # Exercise

# import pandas as pd
# df = pd.read_csv("data.csv", index_col="Name")
# pokemon = input("Enter a Pokemon name: ")
# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} not found")


# ----------------------------------------------------------------------------------------------


# Filtering is when you keep only select rows of a DataFrame that meet a certain condition.

import pandas as pd
df=pd.read_csv("data.csv")

tall_pokemon=df[df["Height"]>=2]
print(tall_pokemon)

legendary_pokemon=df[df["Legendary"]==1]
print(legendary_pokemon)

water_pokemon=df[(df["Type1"]=="Water") | (df["Type2"]=="Water")]
print(water_pokemon)