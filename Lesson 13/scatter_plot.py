import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('avgIQpercountry.csv')

plt.figure(figsize=(10, 6))

plt.scatter(df['Mean years of schooling - 2021'], df['Average IQ'], color='purple', alpha=0.7)

plt.title("Scatter Plot of Mean Years of schooling vs Average IQ", fontsize=16)

plt.xlabel("Mean Years of Schooling - 2021", fontsize=14)

plt.ylabel("Average IQ")

plt.grid(linestyle='--', alpha=0.7)

plt.show()