# %%
import pandas as pd

import os
print("Diretório atual:", os.getcwd())

df = pd.read_csv("c:/Users/ralfr/estudo/analise_gir/Analise_dados_com_pandas/data/products.csv",
                 sep=";",
                 names=["Id", "Name", "Description"]
                 )

df

# %%

df = df.rename(columns={"Name":"Nome",
                        "Description":"Descricao"})

df
# %%

df.rename(columns={"Name": "Nome",
                   "Description": "Descricao"},
                   inplace=True)

df