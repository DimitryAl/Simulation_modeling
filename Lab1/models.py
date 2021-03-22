import math

G = 398603000000000

class TDynamicModel:
    size = 0    

    def get_size(self):
        return self.size
    
    def func(self, values, t):
        raise NotImplementedError()


class TSpaceCraft(TDynamicModel):
    __radius = 0

    def __init__(self):
        self.size = 6

    def func(self, values, t):
        self.rightParts = [0] * self.size

        self.__radius = (values[0]**2 + values[1]**2 + values[2]**2)**(1/2)
        
        self.rightParts[0] = values[3]
        self.rightParts[1] = values[4]
        self.rightParts[2] = values[5]
        self.rightParts[3] = -G * values[0] / self.__radius ** 3 
        self.rightParts[4] = -G * values[1] / self.__radius ** 3 
        self.rightParts[5] = -G * values[2] / self.__radius ** 3 

        return self.rightParts

