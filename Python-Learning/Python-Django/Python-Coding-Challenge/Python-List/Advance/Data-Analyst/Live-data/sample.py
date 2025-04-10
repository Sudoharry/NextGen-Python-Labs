from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime
import time

pytrends = TrendReq()
x_data = []
y_data_dict = {"Facebook": [], "Instagram": [], "TikTok": []}

fig, ax = plt.subplots()
lines = {platform: ax.plot([], [], label=platform)[0] for platform in y_data_dict.keys()}
ax.set_ylim(0, 100)
ax.set_xlim(0, 20)
ax.set_title("Live Google Search Trends: Social Media Platforms")
ax.set_xlabel("Time")
ax.set_ylabel("Trend Score")
ax.legend()

def get_trend_scores():
    pytrends.build_payload(kw_list=list(y_data_dict.keys()), timeframe='now 1-H')
    df = pytrends.interest_over_time()
    if not df.empty:
        return {platform: df[platform].iloc[-1] for platform in y_data_dict.keys()}
    return {platform: 0 for platform in y_data_dict.keys()}

def update(frame):
    trend_scores = get_trend_scores()
    x_data.append(datetime.now().strftime('%H:%M:%S'))
    for platform, score in trend_scores.items():
        y_data_dict[platform].append(score)
        lines[platform].set_data(range(len(x_data)), y_data_dict[platform])
    ax.set_xticks(range(len(x_data)))
    ax.set_xticklabels(x_data, rotation=45, ha='right')
    ax.set_xlim(max(0, len(x_data) - 20), len(x_data))
    return lines.values()

ani = animation.FuncAnimation(fig, update, interval=60000)  # every 60 seconds
plt.tight_layout()
plt.show()