import numpy as np
import os
import matplotlib.pyplot as plt 

from integrators import TRungeKutta
from models import TSpaceCraft

def main():
    integrator = TRungeKutta()
    model = TSpaceCraft()

    values = [31200000.0, 31200000.0, 0.0, -1700.0, 1200.0, -1900.0]    #x,y,z,Vx,Vy,Vz
    tk = 200000
    h = 1
    t = 0
    
    tt = [i for i in range(tk//h)]
    x = []
    y = []
    z = []
    for i in np.arange(t, tk): 
        integrator.oneStep(model, values, t, h)
        x.append(values[0])
        y.append(values[1])
        z.append(values[2])
        t += h
        print(i, end='\n')

    plt.plot(tt, x, label='x')
    plt.plot(tt, y, label='y')
    plt.plot(tt, z, label='z')
    plt.xlabel('t - axis')
    plt.legend()
    plt.show()



if __name__ == "__main__":
    main()