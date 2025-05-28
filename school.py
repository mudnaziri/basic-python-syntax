import pandas as pd

df= pd.read_csv("school.csv")
print(df)

print("Information about the DataFrame:")
print(df.info())

print("Descriptive statistics of the DataFrame:")
print(df.describe())

print("Null value count in dataframe")
print(df.isnull().sum())

corrrelation=df["Age"].corr(df["Score"])
print(f"Correlation B/W Age and Score: {corrrelation}")

df["Score"]=df["Score"].interpolate(method="linear")
df["Age"]=df["Age"].interpolate(method="linear")
print("After interpolate ")
print(df)

df.at[4,"Score"] = 68.0

df.at[4,"Grade"] = "E"

df .at[1,"Passed?"] ="Yes"

df .at[3,"Passed?"] ="Yes"
print(df)

df.to_csv("school_updated.csv", index=False)
print(df)