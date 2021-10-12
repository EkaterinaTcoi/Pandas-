import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("venv/file.csv")

# print row 3-8 (using iloc/loc).
print(df.iloc[3:9])
print(df.loc[3:8])

# find the mean number of all-inclusive hotels across all destinations.
x_mean = df["All-inclusive"].mean()
print(x_mean)

# find the lowest scoring destination.
xl = df["Feedback Score"].min()
print(xl)

# find the highest scoring destination.
xh = df["Feedback Score"].max()
print(xh)

# find all the destinations where there are more than 9 all-inclusive hotels.
allin = df["All-inclusive"] > 9
print(df[["Island, County", "All-inclusive"]][allin])

# filter the data by score above 8
score_a = df["Feedback Score"] > 8
print(df[["Island, County", "Feedback Score"]][score_a])

# filter the data score below 2 (I need to know if these destinations should be removed or there is a problem)
score_b = df["Feedback Score"] < 2
print(df[["Island, County", "Feedback Score"]][score_b])

# filter the data by the possibility of placing childrens
kids = (df["Kids"] == "yes")
print(df[["Island, County", "Kids"]][kids])

# find a correlation between number of all-inclusive and score
df.plot(x="Most Visited Destination ", y=["Feedback Score", "Hotel", "All-inclusive"], kind="bar")
plt.show()

# VD of destination and highest scores
df.plot(x="Most Visited Destination ", y="Feedback Score", kind="bar")
plt.show()

# visualisation for price per weeekend
df.plot(x="Most Visited Destination ", y="Price for weekend", kind="bar")
plt.show()
