import altair as alt
import pandas as pd
import numpy as np

# Create DataFrame
date_range = pd.date_range(start="2025-04-01", periods=30)
data = pd.DataFrame({
    'Date': date_range,
    'Forecasted_Price': np.cumsum(np.random.randn(30) * 5 + 150)
})

# Chart definition
chart = alt.Chart(data).mark_line().encode(
    x='Date:T',
    y='Forecasted_Price:Q'
).properties(
    width=700,
    height=400,
    title="📈 NIFTY 50 Forecast - Next 30 Days"
)

# Save as HTML to view in browser
chart.save("nifty_forecast.html")
print("Chart saved as nifty_forecast.html. Open it in your browser.")
