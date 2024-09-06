# Ada di historyProduksi.py
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

produksi = np.array([1409559.  , 1347611.  , 1557944.  , 1666591.  , 1577398.  ,
       1931505.  , 1789961.  , 1863643.  , 1723433.  , 1899849.  ,
       1977345.  , 2260794.  , 2320110.  , 2456251.  , 2753044.  ,
       2971286.  , 3125236.  , 3272451.  , 3384670.  , 3295247.  ,
       3676723.  , 3670435.  , 4247922.  , 4881089.  , 4807430.  ,
       2994191.84, 2603396.24, 2696877.46])

fig, ax = plt.subplots()
ax.set_xlim(years.min(), years.max())
ax.set_ylim(produksi.min(), produksi.max())
ax.set_xlabel('Year')
ax.set_ylabel('Produksi')
ax.set_title('Produksi Beras (Ton) di Provinsi Sumatera Selatan')
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

plt.show()

ani.save('produksi_animation.gif', writer='ffmpeg', fps=2)