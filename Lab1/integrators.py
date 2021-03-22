from copy import copy
import models

class TAbstractIntegrator:

    def oneStep(self, model, values, t, h):
        raise NotImplementedError()



class TEuler(TAbstractIntegrator):

    def oneStep(self, model, values, t, h):
        self.n = model.get_size()
        self.rightParts = model.func(values, t)

        for i in range(self.n):
            values[i] += h * self.rightParts[i]
    

class TRungeKutta(TAbstractIntegrator):

    def oneStep(self, model, values, t, h):
        self.n = model.get_size()

        for i in range(self.n):
            self.temp = copy(values)
            
            self.k1 = model.func(self.temp, t)
            for j in range(self.n):
                self.temp[j] = values[j] + h * self.k1[j] / 2
            
            self.k2 = model.func(values, t + h / 2)
            for j in range(self.n):
                self.temp[j] = values[j] + h * self.k2[j] / 2
            
            self.k3 = model.func(self.temp, t + h / 2)
            for j in range(self.n):
                self.temp[j] = values[j] + h * self.k3[j] / 2
            
            self.k4 = model.func(self.temp, t + h)
            values[i] += h * (self.k1[i] / 6 + self.k2[i] / 3 + self.k3[i] / 3 + self.k4[i] / 6)