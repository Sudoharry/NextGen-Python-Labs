import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and clean dataset
df = pd.read_csv(r"C:\Users\Nilesh\.cache\kagglehub\datasets\samybaladram\multidisciplinary-csv-datasets-collection\versions\5\homes.csv")
df.columns = df.columns.str.replace('"', '').str.strip()

# Compute correlation matrix
corr = df.corr(numeric_only=True)

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, square=True)

plt.title("🔍 Feature Correlation Heatmap", fontsize=16)
plt.tight_layout()
plt.show()
