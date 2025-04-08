import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"C:\Users\Nilesh\.cache\kagglehub\datasets\samybaladram\multidisciplinary-csv-datasets-collection\versions\5\homes.csv"
df = pd.read_csv(file_path)
df.columns = df.columns.str.replace('"', '').str.strip()


# # Preview the data
# print(df.head())
# print("\nSummary Info:")
# print(df.info())


plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

sns.scatterplot(data=df, x='Living', y='Sell')
plt.title('Sell Price vs Living Area')
plt.xlabel('Living Area (x100 sq ft)')
plt.ylabel('Sell Price (in thousands)')
plt.show()


sns.lmplot(data=df, x='Living', y='Sell')
plt.title('Linear Relationship: Living Area vs Sell Price')
plt.xlabel('Living Area')
plt.ylabel('Sell Price')
plt.show()