import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import NullFormatter

def formatter(x, pos):
    if x >= 1e6:
        return str(round(x / 1e6, 1)) + " Juta"
    return x

years = np.array([1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 
                  2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 
                  2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020])

produksi = np.array([1646900.00, 1615751.00, 1943709.00, 1971740.00, 1753656.00, 1975700.00, 
                     1801422.00, 1946406.00, 1992726.00, 1951109.00, 1966293.00, 2091996.00, 
                     2124144.00, 2129914.00, 2308404.00, 2341075.00, 2673844.00, 2807676.00, 
                     2940795.00, 3101455.00, 3207002.00, 3320064.00, 3641895.00, 3831923.00, 
                     4090654.00, 2488641.91, 2164089.33, 2604913.29])

fig, ax = plt.subplots()
ax.set_xlim(years.min(), years.max())
ax.set_ylim(produksi.min(), produksi.max())
ax.set_xlabel('Year')
ax.set_ylabel('Produksi')
ax.set_title('Produksi Beras (Ton) di Provinsi Lampung')
plt.grid(True, alpha=0.3)

line, = ax.plot([], [], lw=2)
ax.yaxis.set_major_formatter(formatter)
ax.yaxis.set_minor_formatter(NullFormatter())

# Initialization function for the animation
def init():
    line.set_data([], [])
    return line,

# Animation function, updating the plot
def update(frame):
    x_data = years[:frame]
    y_data = produksi[:frame]
    line.set_data(x_data, y_data)
    
    # Determine the color of the line based on trend
    if frame > 1:
        # Check if the trend is increasing or decreasing
        if y_data[-1] >= y_data[-2]:
            line.set_color('green')
        else:
            line.set_color('red')
    
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=len(years), init_func=init, blit=True, interval=500)

ani.save('produksi_animation.gif', writer='ffmpeg', fps=2)