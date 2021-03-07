from TVector import TVector

class TDynamicModel:

    RightParts = TVector

    # конструктор
    def __init__(self, vector):
        self.RightParts = vector
    
    # изменить значения вектора
    # def change_vec(self, vector):
    #     self.RightParts = vector
    
    # 
    def get_RightParts(self, value):
        raise NotImplementedError()