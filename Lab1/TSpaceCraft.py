from TDynamicModel import TDynamicModel
from copy import copy

# гравитацционная постоянная
m = 3.98603*(10**14)

class TSpaceCraft(TDynamicModel):

    def get_RightParts(self, value):
        r = (value[0]**2 + value[1]**2 + value[2]**2)**(1/2)

    