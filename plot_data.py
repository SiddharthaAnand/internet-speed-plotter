#Note: Here X axis will show the total timecount ( i.e. second)
#Note: Here Y aixs will show the value of speed of your internet

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')
count = 10 #At max how many values can be shown in the current live graph
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('speed.csv','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    y = 0
    for line in lines:
        if len(line) > 1:
            x, temp1, temp2 = line.split(',')
            y = y+1
            xs.append(x)
            ys.append(y)
    xs = xs[-(count):]
    ys = ys[-(count):]
    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
