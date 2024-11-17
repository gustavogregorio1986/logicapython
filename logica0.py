import pandas as pd

dados = [10,20,30,40]

vetor = pd.Series(dados)
print(vetor)

print(vetor + 10)
print(vetor * 2)

print(vetor.sum())
print(vetor.mean())
print(vetor.max())
