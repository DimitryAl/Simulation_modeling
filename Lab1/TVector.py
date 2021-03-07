
class TVector(): # класс для вектора состояний
    
    # x = 0
    # y = 0
    # z = 0
    # vx = 0
    # vy = 0
    # vz = 0

    # конструктор
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

    # умножить вектор на число
    def mult(self, n):
        self.x *= n
        self.y *= n
        self.z *= n
        self.vx *= n
        self.vy *= n
        self.vz *= n
        
    # прибавить число/вектор к вектору 
    def add(self, n):
        if isinstance(n, TVector):
            self.x += n.x
            self.y += n.y
            self.z += n.z
            self.vx += n.vx
            self.vy += n.vx
            self.vz += n.vz
        if isinstance(n, float or int):
            self.x += n
            self.y += n
            self.z += n
            self.vx += n
            self.vy += n
            self.vz += n

    # вернуть вектор (тип turple) 
    def get(self):
        return (self.x, self.y, self.z, self.vx, self.vy, self.vz)
    
    # из массива в TVector
    def set_vector(self, vector):
        self.x = vector[0]
        self.y = vector[1]
        self.z = vector[2]
        self.vx = vector[3]
        self.vy = vector[4]
        self.vz = vector[5]