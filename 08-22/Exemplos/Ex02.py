import numpy as np
import pandas as pd
from pandas import Series,DataFrame

data = {"Estado":["São Paulo","Santa Catarina","Bahia","Goias","Rio Grande do Sul","Parana"],
        "Ano"   :[2012,2014,2016,2018,2020,2022],
        "População":[10000,12000,9000,15000,19000,8000]}
frme1 = DataFrame(data,
                 columns = ["Ano","Estado","População","Debito"],
                 index=["1","2","3","4","5","6"])
frme1["Debito"] = np.arange(6.)

frme1[:2]


evento = {"Dias":[1,2,3,4,5,6,7],
          "Visitantes":[23,45,12,65,98,57,76],
          "Taxas":[11,22,33,44,55,66,77]}
frme2 = DataFrame(evento)
frme2[["Visitantes","Taxas"]]