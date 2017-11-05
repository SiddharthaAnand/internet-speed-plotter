import matplotlib.pyplot as plot
import matplotlib.animation as animation

figure = plot.figure()
axis = figure.add_subplot(1, 1, 1)

def animate_plot(x):
	axis.clear()
	axis.plot(x)

ani = animation.FuncAnimation(figure, animate_plot, interval = 60)
plot.show()