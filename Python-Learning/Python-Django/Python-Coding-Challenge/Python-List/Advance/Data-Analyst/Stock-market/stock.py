import yfinance as yf
from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt


nifty = yf.download("^NSEI", start="2022-01-01", interval="1D")

df = nifty.reset_index()[['Date', 'Close']]
df.columns = ['ds', 'y']

model = Prophet()
model.fit(df)

future = model.make_future_dataframe(periods=7)
forecast = model.predict(future)
model.plot(forecast)

fig = model.plot(forecast)
plt.title("📈 NIFTY 50 - Next 7 Days Forecast", fontsize=16)
plt.xlabel("Date")
plt.ylabel("Closing Price (INR)")
plt.grid(True)
plt.tight_layout()
plt.show()