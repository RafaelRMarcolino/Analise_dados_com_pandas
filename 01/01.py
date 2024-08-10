# %%
print('Anlise de dados Pandas')

# %%

from statistics import median
import pandas as pd

# %%

idades = [30, 42, 90, 34]
idades

# %%

media = sum(idades) / len(idades)

# %%
#desvio padrão

total = 0
for i in idades:
    total += (media -1) **1

variancia = total / (len(idades) - 1)

print(variancia)


# %%

series_idades = pd.Series(idades)
series_idades

# %%
series_idades.mean()

# %%
series_idades.var()

# %%

series_idades.median()

series_idades.std()


series_idades.describe


series_idades.shape

#trocar indices
series_idades.index = ['r', 'a', 'f', 'e']

series_idades[2]
series_idades.describe

#iloc pega pela posição permite que voce pague os dados mesmo se o indidece estiver embatalhjado o iloc garante o que vc esta pegando esta certo
series_idades.iloc[0:2]

# Pega pelo indice
# series_idades.loc[0]

