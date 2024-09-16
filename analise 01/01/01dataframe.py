# %%
import pandas as pd

data = {
    "nome": ["teo", "nah", "iara", "maria"],
    "sobrenome": ["teste", "teste2", "teste3", "teste4"],
    "idade": [1, 2, 58, 56]
}

df = pd.DataFrame(data)

df

df["idade"]

#para garantir que estou pegando esta certo
df["idade"].iloc[0]

df.index = [2, 1, 0, 3]

df.iloc[0]


#para saber o nome das colunas
df.columns

df.info()