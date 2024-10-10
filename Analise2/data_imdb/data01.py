import pandas as pd
import numpy as np

sexo = {0: 'Masculino', 1: 'Feminino'}
cor = {0: 'Indigena', 1: 'Branca', 3: 'Preta', 4: 'Amarela', 5: 'Parda', 6: 'Sem Declaração'}

ufs = [
    'AC',  # Acre
    'AL',  # Alagoas
    'AP',  # Amapá
    'AM',  # Amazonas
    'BA',  # Bahia
    'CE',  # Ceará
    'DF',  # Distrito Federal
    'ES',  # Espírito Santo
    'GO',  # Goiás
    'MA',  # Maranhão
    'MT',  # Mato Grosso
    'MS',  # Mato Grosso do Sul
    'MG',  # Minas Gerais
    'PA',  # Pará
    'PB',  # Paraíba
    'PR',  # Paraná
    'PE',  # Pernambuco
    'PI',  # Piauí
    'RJ',  # Rio de Janeiro
    'RN',  # Rio Grande do Norte
    'RS',  # Rio Grande do Sul
    'RO',  # Rondônia
    'RR',  # Roraima
    'SC',  # Santa Catarina
    'SP',  # São Paulo
    'SE',  # Sergipe
    'TO'   # Tocantins
]

num = 1000

data = {
    'UF': np.random.choice(ufs, num),
    'Sexo': np.random.choice(list(sexo.values()), num),
    'Idade': np.random.randint(18, 70, num),
    'Cor': np.random.choice(list(cor.values()), num),
    'Anos de estudo': np.random.randint(0, 21, num),  # De 0 a 20
    'Renda': np.random.randint(1000, 20000, num),
    'Altura': np.random.uniform(1.5, 2.0, num).round(2)
}

df = pd.DataFrame(data)

print(df.head(100))
