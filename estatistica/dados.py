import pandas as pd
import numpy as np

def dados_fake():
    sexo = {0: 'Masculino', 1: 'Feminino'}
    cor = {0: 'Indigena', 1: 'Branca', 3: 'Preta', 4: 'Amarela', 5: 'Parda', 6: 'Sem Declaração'}

    ufs = [
        'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
        'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN',
        'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
    ]

    num = 30

    dados_fake = {
        'UF': np.random.choice(ufs, num),
        'Sexo': np.random.choice(list(sexo.values()), num),
        'Idade': np.random.randint(18, 70, num),
        'Cor': np.random.choice(list(cor.values()), num),
        'Anos de estudo': np.random.randint(0, 21, num),
        'Renda': np.random.randint(1000, 20000, num),
        'Altura': np.random.uniform(1.5, 2.0, num).round(2)
    }

    return pd.DataFrame(dados_fake)

