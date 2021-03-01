
# t == x
# X == y


#функция
def func(t, x):    
    return t * x

#метод Эйлера
def Euler(X, n, h, t):
    res = []        #массив с значениями 
    res.append(X)       
    temp = X.copy()     
    for i in range(n):
        t = t + i * h
        for j in range(len(X)):
            temp[j] = res[i][j] + h * func(t, res[i][j])
        res.append(temp.copy())
    return res

#метод Рунге-Кутты
def Runge_Kutta(X, n, h, t):
    res = []
    res.append(X)
    temp = X.copy()
    for i in range(n):
        k1 = [0]*len(X)
        k2, k3, k4 = k1.copy(), k1.copy(), k1.copy()
        for j in range(len(X)):
            k1[j] = func(t, res[i][j])
            k2[j] = func(t + h / 2, res[i][j] + h / 2 * k1[j])
            k3[j] = func(t + h / 2, res[i][j] + h / 2 * k2[j])
            k4[j] = func(t + h, res[i][j] + h * k3[j])
            temp[j] = res[i][j] + h / 6 *(k1[j] + k2[j] + k3[j] + k4[j]) 
        res.append(temp.copy())
    return res
    
#начальный вектор состояния КА в абсолютной СК
#X = [x, y, z, Vx, Vy, Vz]
#начальный вектор ускорений
#a = [ax, ay, az]
#print(Euler([1, 2, 1], 5, 0.5, 1))
print(Runge_Kutta([1, 2, 1], 5, 0.5, 1))
