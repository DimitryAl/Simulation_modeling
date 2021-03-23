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
        if i % 1000 == 0:
            print('\r', end='')
            print('Progress: %.1f' % (i/tk*100), '%', end='')
        integrator.oneStep(model, values, t, h)
        x.append(values[0])
        y.append(values[1])
        z.append(values[2])
        t += h

    # запись координат в файлы
    fx = open('x.txt', 'w')
    fy = open('y.txt', 'w')
    fz = open('z.txt', 'w')
    for i in range(len(x)):
        fx.write(str(x[i]) + '\n')
        fy.write(str(y[i]) + '\n')
        fz.write(str(z[i]) + '\n')
    fx.close()
    fy.close()
    fx.close()
    
    # вывод графика в файл
    plt.title('Зависимость координат от времени')
    plt.plot(tt, x, label='x')
    plt.plot(tt, y, label='y')
    plt.plot(tt, z, label='z')
    plt.xlabel('t')
    plt.legend()
    plt.savefig('result.png')
    plt.show()

    print('Done')

if __name__ == "__main__":
    print('Program start')
    main()
    print('Program end')