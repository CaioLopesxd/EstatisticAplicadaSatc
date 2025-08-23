import numpy as np
import pandas as pd
from pandas import Series,DataFrame

matriz = np.array([[1,2,3],
                   [1,2,3]])
resultado = matriz * 2

srie = Series([4,7,-5,3])
srie2 = Series([4,7,-5,3], index=['a','b','c','d'])
srie2[srie2 > 3]
srie2[srie2 < 3]

dicio = {"Futebol":5200,"Tenis":1200,"Natação":1698,"Basketball":2000}
srie3 = Series(dicio)
esportes = ["Futebol","Tenis","Natação","Basketball","Volei"]
srie4 = Series(dicio,index=esportes)
pd.notnull(srie4)

srie4 + srie3
srie4.name = "População"
srie4.index.name = "Esportes"
srie4    

