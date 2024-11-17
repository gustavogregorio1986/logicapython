import pandas as pd

dados = {
    "Nome":["Luiz","maycon","Marcelo","Michelle","Mirele", "Marcel", "Mario", "Marcos"],
    "Idade":[23,43,12,43,12,34,32,23],
    "Sexo":["Masculino","Masculino","Masculino","Feminino","Feminino","Masculino","Masuclino", "masculino"],
}

df = pd.DataFrame(dados)

alistamento = (df["Idade"] > 18) & (df["Sexo"] == "Masculino")

print(alistamento)