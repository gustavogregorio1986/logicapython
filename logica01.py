import pandas as pd

dados = {
    "Nome":["Luiz","Pedro","Marcos","Mirele", "Matheus", "Michelle", "Mycon", "Maria"],
    "Idade":[23,43,23,65,23,12,43,14]
}

df = pd.DataFrame(dados)

maiores_de_18 = df[df["Idade"] > 18]

print(maiores_de_18)

df['MaiorDe18'] = df['Idade'] > 18
print(df)