import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

def load_and_analyze(file_path, team):
    # Carregar o conjunto de dados
    data = pd.read_csv(file_path)

    # Selecionar colunas relevantes para a análise de regras de associação
    if team == "blue":
        selected_columns = [
            "blueWins", "blueFirstBlood", "blueFirstDragon", "blueFirstBaron", "blueFirstInhibitor"
        ]
    elif team == "red":
        selected_columns = [
            "redWins", "redFirstBlood", "redFirstDragon", "redFirstBaron", "redFirstInhibitor"
        ]
    else:
        print("Escolha de time inválida. Encerrando.")
        return
    data_selected = data[selected_columns]

    # Encontrar os conjuntos frequentes usando o algoritmo Apriori
    frequent_itemsets = apriori(data_selected, min_support=0.1, use_colnames=True)

    # Gerar as regras de associação
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)

    # Exibir as regras de associação, incluindo suporte e confiança
    for index, row in rules.iterrows():
        print("Regra:", row["antecedents"], "->", row["consequents"])
        print("Suporte:", row["support"])
        print("Confiança:", row["confidence"])
        print("----")

# Solicitar ao usuário que escolha um arquivo
print("Escolha um arquivo para análise:")
print("1. challenger.csv")
print("2. master.csv")
print("3. grandmaster.csv")
choice_file = input("Digite o número correspondente ao arquivo: ")

if choice_file == "1":
    file_name = "challenger.csv"
elif choice_file == "2":
    file_name = "master.csv"
elif choice_file == "3":
    file_name = "grandmaster.csv"
else:
    print("Escolha de arquivo inválida. Encerrando.")
    exit()

print("Escolha o time para análise:")
print("1. Time Azul (Blue Team)")
print("2. Time Vermelho (Red Team)")
choice_team = input("Digite o número correspondente ao time: ")

if choice_team == "1":
    load_and_analyze(file_name, "blue")
elif choice_team == "2":
    load_and_analyze(file_name, "red")
else:
    print("Escolha de time inválida. Encerrando.")
