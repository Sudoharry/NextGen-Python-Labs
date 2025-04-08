import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load and clean dataset
df = pd.read_csv(r"C:\Users\Nilesh\.cache\kagglehub\datasets\samybaladram\multidisciplinary-csv-datasets-collection\versions\5\homes.csv")
df.columns = df.columns.str.replace('"', '').str.strip()

# Plot
plt.figure(figsize=(12, 7))
sns.scatterplot(
    data=df,
    x='Living',
    y='Sell',
    size='Rooms',
    hue='Beds',
    palette='viridis',
    sizes=(50, 500),
    legend='brief'
)

plt.title('🏡 Sell Price vs Living Area (Bubble = Rooms, Color = Beds)', fontsize=14)
plt.xlabel('Living Area (x100 sq ft)')
plt.ylabel('Sell Price (in $1000s)')
plt.legend(title='Number of Beds & Rooms', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
