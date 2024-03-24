import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib import dates as mdates

df = pd.read_csv('./data/filtered/Yogyakarta.csv')

df['datetime'] = pd.to_datetime(df.iloc[:, 2])
df.sort_values('datetime', inplace=True)
df.set_index('datetime', inplace=True)

rolling_window = 4
df['temperature'] = df.iloc[:, 6]
df['rolling_avg'] = df['temperature'].rolling(window=rolling_window, center=False).mean()

plt.figure(figsize=(14, 7))
plt.plot(df.index, df['temperature'], alpha=0.5, label='Actual Temperature')

plt.plot(df.index, df['rolling_avg'], color='red', label='Rolling Average (4 measurements)')

plt.title('Temperature Trend with Rolling Average in Yogyakarta')
plt.xlabel('Time')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.gcf().autofmt_xdate() 

plt.show()