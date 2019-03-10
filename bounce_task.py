import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



dots = np.random.rand(1000,4)
dots[:,2:] -= 0.5
dots[:,2:] *= 0.01



def main():
    fig, ax = plt.subplots()

    ax.set_xlim(0,1)
    ax.set_ylim(0,1)
    
    xs = dots[:,0]
    ys = dots[:,1]
    
    line, = ax.plot([],[],'b.',ms=16)
    
    def animate(i):
        timestep()
        line.set_data(xs,ys)  # update the data
        return line,
    
    ani = animation.FuncAnimation(fig, animate, 
                                  interval=25, 
                                  blit=True)

    # ani.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
    # or
    plt.show()

def timestep():
    dots[:,:2] += dots[:,2:]

    # gravity
    # dots[:,3]  -= 0.001

    # bounce off walls
    # cross_left  = dots[:,0] < 0.
    # ...

    # collision()





main()


# Based on 
#
# Animation of Elastic collisions with Gravity
# 
# author: Jake Vanderplas
# email: vanderplas@astro.washington.edu
# website: http://jakevdp.github.com
# license: BSD
# Please feel free to use and modify this, but keep the above information. Thanks!

