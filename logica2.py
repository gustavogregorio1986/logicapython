import pandas as pd

dados = {
    "Nome": ["Luiz", "Maycon", "Marcelo", "Michelle", "Mirele", "Marcel", "Mario", "Marcos"],
    "Idade": [23, 43, 12, 43, 12, 34, 32, 23],
    "Sexo": ["Masculino", "Masculino", "Masculino", "Feminino", "Feminino", "Masculino", "Masuclino", "masculino"],
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Condição para alistamento
alistamento = (df["Idade"] > 18) & (df["Sexo"] == "Masculino")

# Filtrar apenas as pessoas aptas ao alistamento
pessoas_alistadas = df[alistamento]

# Exibir as pessoas alistadas
print("Pessoas aptas ao alistamento:")
print(pessoas_alistadas)
