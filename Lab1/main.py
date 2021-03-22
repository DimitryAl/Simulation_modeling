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
    
    f = open('test.txt', 'w')

    for i in np.arange(t, tk): 
        integrator.oneStep(model, values, t, h)
        # print('t = \t', t, end='\n')
        # print("y(t): ", end='\n')
        # for j in range(len(values)):
        #     print(values[j], end='\n')
        # print('\n')
        #f.write(str(i) + ' ' + str(values[0]) + '\n')
        t += h
        print(i, end='\n')

    x = [i for i in range(tk/h)]
    y = []
    for i in range(tk/h):
        y.append(values[i][0])
    plt.plot(x, y)
    plt.show()
    #print('\nSteps: ', i, end='\n')
    f.close()


if __name__ == "__main__":
    main()