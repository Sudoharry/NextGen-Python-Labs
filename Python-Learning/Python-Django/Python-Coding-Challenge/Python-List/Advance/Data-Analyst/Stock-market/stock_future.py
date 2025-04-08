import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

# Create future date range
start_date = datetime.today()
dates = [start_date + timedelta(days=i) for i in range(7)]

# Generate dummy closing prices using trend + noise
np.random.seed(42)
base_price = 22500
trend = np.linspace(0, 150, 7)  # Upward trend
noise = np.random.normal(0, 50, 7)  # Market noise
closing_prices = base_price + trend + noise

# Create DataFrame
forecast_df = pd.DataFrame({
    'Date': [d.date() for d in dates],
    'NIFTY_50_Closing_Price': closing_prices.round(2)
})

print(forecast_df)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(forecast_df['Date'], forecast_df['NIFTY_50_Closing_Price'], marker='o', linestyle='-')
plt.title('Simulated NIFTY 50 Closing Price Forecast (Next 7 Days)')
plt.xlabel('Date')
plt.ylabel('Closing Price (₹)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
