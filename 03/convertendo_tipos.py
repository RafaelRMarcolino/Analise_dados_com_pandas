# %%
import pandas as pd

import os
print("Diretório atual:", os.getcwd())

df = pd.read_csv("../data/customers.csv", sep=";")
df
# %%

df.dtypes


# %%

df["Points_dobble"] = df["Points"] * 2

# %%
df[["Points", "Points_dobble"]].astype(float)

# %%
df[["UUID", "Name"]].astype(int)

# %%

df["Lista"] = [[ 1,2 ] for i in df.index ]
df

# %%

df.dtypes