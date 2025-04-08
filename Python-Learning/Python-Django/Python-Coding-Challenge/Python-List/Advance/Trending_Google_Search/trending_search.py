# # pip install pytrends

from pytrends.request import TrendReq
import pandas as pd
import time

# Set future behavior warning fix
pd.set_option('future.no_silent_downcasting', True)

# Supported region list with ISO country codes
region_map = {
    "united_states": "US",
    "germany": "DE",
    "india": "IN",
    "united_kingdom": "GB",
    "japan": "JP",
    "france": "FR",
    "brazil": "BR",
    "australia": "AU",
    "canada": "CA",
    "south_korea": "KR"
}

# Show available regions
print("Available regions:")
for region in region_map:
    print(f"- {region}")

# Get user input
region = input("\nEnter the region from above: ").strip().lower()

# Validate input
if region not in region_map:
    print("❌ Invalid region. Please choose from the list above.")
else:
    try:
        # Choose some global-interest keywords
        kw_list = ["AI", "Bitcoin", "Cricket", "Python", "Elections"]

        print(f"\n📡 Fetching trending data for: {region.title()}...\n")
        pytrends = TrendReq()
        time.sleep(1)  # Respectful delay

        pytrends.build_payload(kw_list, timeframe='now 1-d', geo=region_map[region])
        data = pytrends.interest_over_time()

        if data.empty:
            print("⚠️ No data returned for the selected region and keywords.")
        else:
            latest = data.iloc[-1].drop("isPartial")
            print("🔥 Top Keywords (Most searched right now):")
            print(latest.sort_values(ascending=False))

    except Exception as e:
        print("❌ Failed to fetch trending data. Error:", e)

# from pytrends.request import TrendReq

# pytrends = TrendReq()

# kw_list = ["AI", "Bitcoin", "Cricket", "Python", "Elections"]
# pytrends.build_payload(kw_list, cat=0, timeframe='now 1-d', geo='DE', gprop='')

# # Get interest over time
# interest = pytrends.interest_over_time()

# if not interest.empty:
#     print("Top Trends in Germany (past 24h):")
#     print(interest.head())
# else:
#     print("No data found.")
