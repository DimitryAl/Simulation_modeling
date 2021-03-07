from TVector import TVector
from TDynamicModel import TDynamicModel
from TEuler import TEuler
from TAbstractIntegrator import TAbstractIntegrator

vector1 = TVector(1, 1, 1, 1, 1,1)

model = TDynamicModel(vector1)

integ = TEuler(0, 10, 0.01, model)

for i in range(10):
    integ.OneStep()
    