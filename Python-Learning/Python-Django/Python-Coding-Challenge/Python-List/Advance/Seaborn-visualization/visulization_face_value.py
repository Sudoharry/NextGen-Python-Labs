import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load and clean CSV
df = pd.read_csv(r"C:\Users\Nilesh\Downloads\EQUITY_L.csv")
df.columns = df.columns.str.strip()  # Remove extra spaces

# Convert FACE VALUE to numeric (just in case it's not)
df['FACE VALUE'] = pd.to_numeric(df['FACE VALUE'], errors='coerce')

# Sort by FACE VALUE (optional) and take top 10 for clarity
top_stocks = df.sort_values(by='FACE VALUE', ascending=False).head(10)

# Plot
plt.figure(figsize=(10, 6))
sns.barplot(data=top_stocks, x='SYMBOL', y='FACE VALUE', palette='viridis')
plt.title('Top 10 Stocks by Face Value')
plt.xlabel('Stock Symbol')
plt.ylabel('Face Value (₹)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
