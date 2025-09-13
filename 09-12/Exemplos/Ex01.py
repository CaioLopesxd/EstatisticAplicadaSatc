import numpy as np
import random
import pandas as pd

dataset = pd.read_csv("census.csv")
random.seed(1)
i = random.randint(0,325)
i
np.arange(i,len(dataset),step=325)

def amostragem_sistematica(dataset, amostras):
    intervalo = len(dataset) // amostras
    random.seed(1)
    inicio = random.randint(0, intervalo)
    indices = np.arange(inicio, len(dataset), step = intervalo)
    amostra_sistematica = dataset.iloc[indices]
    return amostra_sistematica

amostra_sistematica = amostragem_sistematica(dataset, 100)
amostra_sistematica.shape
amostra_sistematica.head()