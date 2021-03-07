from TVector import TVector

class TAbstractIntegrator:

    # конструктор
    def __init__(self, t0, tk, h, RightParts):
        self.t0 = t0
        self.tk = tk
        self.h = h
        self.Model = RightParts
    
    def SetRightParts(self, RightParts):
        self.Model = RightParts
    
    def MoveTo(self):
        raise NotImplementedError()

    def OneStep(self):
        raise NotImplementedError()

    



