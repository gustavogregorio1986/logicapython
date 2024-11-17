import pandas as pd

dados = {
    "Cidade":["Rio de Janeiro","Sao Paulo","Salvador","Curitiba","Aracaju"],
    "Regiao":["Sudeste","Sudeste","Nordeste","Sul","Nordeste"]
}

df = pd.DataFrame(dados)

print(df)

regiaoSul = df[df["Regiao"] == "Sul"]

regiaoSudeste = df[df["Regiao"] == "Sudeste"]

print(regiaoSul)

print(regiaoSudeste)