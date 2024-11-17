import pandas as pd

dados = {
    "Nome":["Luiz","Pedro","mario","Michel","Mirele","Bruno"],
    "Idade":[34,32,34,54,23,43]
}

df = pd.DataFrame(dados)

print(df)