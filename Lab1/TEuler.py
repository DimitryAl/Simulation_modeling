from TAbstractIntegrator import TAbstractIntegrator
from copy import copy

class TEuler(TAbstractIntegrator):

    def OneStep(self):
        temp = copy(self.Model.RightParts)
        temp.mult(self.h)
        self.Model.RightParts.add(temp)

    