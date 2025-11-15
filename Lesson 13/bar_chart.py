import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../avgIQpercountry.csv')

filtered_df = df[df["Average IQ"]>= 100]

filtered_df = filtered_df.sort_values(by="Average IQ", ascending= False)

print(fildered_df)

plt.figure(figsize=(14,8))

bar = plt.bar(filtered_df["Country"], filtered_df["Average IQ"], color='skyblue')

plt.title("Average IQ by country (iQ >= 100)", fontsize=16)

plt.xlabel("Country", fontsize=14)
plt.ylabel("Average IQ", fontsize=14)

plt.tight_layout()