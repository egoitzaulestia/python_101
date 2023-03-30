import pandas as pd
import numpy as np

df = pd.read_csv("https://raw.githubusercontent.com/sivabalanb/Data-Analysis-with-Pandas-and-Python/master/fortune1000.csv")

df.loc[3]

df.tail()

df.loc[500:504]

df.loc[500:504, ["Company", "Sector"]]

df.loc[(df["Revenue"] >= 14_000) & (df["Revenue"] <= 20_000), ["Company", "Location", "Revenue"]]

df.loc[(df["Revenue"] >= 14_000) & (df["Revenue"] <= 20_000), ["Company", "Location", "Revenue"]].sort_values("Revenue", ascending = False)

# df1 = df.loc[df["Revenue"] >= 14_000]
# df2 = df1.loc[df["Revenue"] <= 20_000]
# df3 = df2.sort_values("Revenue", ascending = False)
# df3.head()
# df_final = df3[["Company", "Revenue"]]
# df_final.head()

df1 = df.loc[(df["Sector"] == "Technology") & (df["Employees"] > 100_000)]
df1.plot.bar(x = "Company", y = "Employees")
