import pandas as pd
import numpy as np


def header(msg):
    print("-" * 50)
    print(" [ " + msg + " ] ")


def footer():
    print("-" * 50)


# ==== Dataframes in pandas =====

# 1. load hard-coded data into a df
header("1. load hard-coded data into a df")
df = pd.DataFrame(
    [
        ["Jan", 12, 45, 66],
        ["Feb", 12, 34, 56],
        ["Mar", 23, 45, 32],
        ["Apr", 34, 56, 23],
        ["May", 12, 45, 66],
        ["June", 12, 34, 56],
        ["July", 23, 45, 32],
        ["Aug", 34, 56, 23],
    ],
    index=[0, 1, 2, 3, 4, 5, 6, 7],
    columns=["month", "count", "temp", "humidity"],
)
print(df)
footer()

# 2. load external file data into a df
header("2. load external file data into a df")
file_name = "months.csv"

df = pd.read_csv(file_name)

print(df)
footer()

# 3. get first 5 and last 3 data from a df
header("3. get first 5 and last 3 data from a df")

header("3.1. df.head() ")
print(df.head())  # default to 5 data elements

header("3.2. df.tail() ")
print(df.tail())

header("3.3. df.tail(3) ")
print(df.tail(3))  # last 3 elements
footer()

# 4. get metadata from the df

header("4.1 Get indexes")
print(df.index)

header("4.2 Get Datatypes")
print(df.dtypes)

header("4.3 Get columns")
print(df.columns)

header("4.4 Get values")
print(df.values)
footer()

# 5. get statistical data from the df

header("5. Get stats")
print(df.describe())
footer()

# 6. sort df data

header("6. Sort values")
print(df.sort_values("humidity", ascending=False))
footer()

# 7. slicing data

header("7. slicing data")
header("7.1 slicing by dot method")
print(df.month)

header("7.2 slicing by bracker method")
print(df["month"])

header("7.3 slicing by giving range method")
print(df[2:4])  # [id1:id2) => id1 to id2 , but exclusive of id2

header("7.4 slicing by mentioning columns")
print(df[["month", "humidity"]])

header("7.5 slicing by mentioning columns")
print(df[["month", "humidity"]])

header("7.6 slicing by mentioning locations")
print(df.loc[:, ["humidity"]])  # df.loc[from_row:to_row,['col1','col2]]

header("7.7 slicing by scalar value")
print(df.loc[4, ["humidity", "month"]])  # df.loc[row_idx,['col1','col2]]

header("7.7 slicing by range of rows and indexes of columns")
print(df.iloc[2:4, [0, 2]])  # df.iloc[row_idx2:row_idx2,[col1:col2]]

footer()

# 8. Filtering

header("8. Filtering data")

header("8.1 Filtering data on column values")
print(df[df.temp < 45.0])  # filter on column values


header("8.2 Filtering data on column ranges")
print(df[df["month"].isin(["Jan", "Feb"])])

footer()

# 9. Assignment

header("9. Assignment")

header("9.1 Set by location")
df.loc[2, ["count"]] = 86
print(df)

header("9.2 Set nan")
df.loc[3, ["count"]] = np.nan
print(df)

header("9.3 Set all columns")
df.loc[:, "temp"] = np.add(5, 6)
print(df)

footer()

# 10. Renaming columns

header("10. Renaming")

header("10.1 Renaming by rename()")
df.rename(
    columns={"temp": "curr_temp"}, inplace=True
)  # inplace is to save it to the curr df

print(df.head())
footer()

header("10.2 Mentioning all columns")
df.columns = ["months", "counts", "temps", "humid"]

print(df.head())
footer()

# 11. Iterate rows in df

header("11. Iterate rows in df")

for index, row in df.iterrows():
    print(index, row["months"], row["counts"])

footer()

# 12. Iterate rows in df

header("12. Write to file")

df.to_csv("output.csv")
