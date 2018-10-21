from datetime import datetime
import csv
import numpy as np
import itertools
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import time

speeds = []
dates = []

with open('speed.csv', 'rb') as csvfile:
	lines = itertools.islice(csvfile, 1, None)
	spamreader = csv.reader(lines, delimiter=',', quotechar='|')
	for row in spamreader:
		speed = row[0]
		date_str = row[2]
		dt_obj = datetime.strptime(date_str, "%a %b %d %X %Y")
		speeds.append(speed)
		dates.append(dt_obj)

fig, ax = plt.subplots()
ax.plot(dates, speeds)
datemin = np.datetime64(dates[0], 'm')
datemax = np.datetime64(dates[-1], 'm') + np.timedelta64(1, 'm')
ax.set_xlim(datemin, datemax)

def mbs(x):
    return x
ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.format_ydata = mbs
ax.grid(True)

fig.autofmt_xdate()

plt.show()