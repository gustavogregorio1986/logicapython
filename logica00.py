import pandas as pd

dados = [10, None, 30, 40, None]
vetor = pd.Series(dados)
print(vetor.fillna(0))