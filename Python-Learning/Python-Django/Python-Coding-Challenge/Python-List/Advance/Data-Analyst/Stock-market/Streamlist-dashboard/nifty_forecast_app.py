import yfinance as yf
from prophet import Prophet
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("📈 NIFTY 50 - 7 Day Forecast")

# Download data
nifty = yf.download("^NSEI", start="2022-01-01", interval="1d")
df = nifty.reset_index()[['Date', 'Close']]
df.columns = ['ds', 'y']

# Prophet model
model = Prophet()
model.fit(df)

# Forecast next 7 days
future = model.make_future_dataframe(periods=7)
forecast = model.predict(future)

# Plot
fig = model.plot(forecast)
plt.title("NIFTY 50 Forecast")
st.pyplot(fig)
