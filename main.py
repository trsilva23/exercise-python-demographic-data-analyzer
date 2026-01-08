# main.py para testar a função calculate_demographic_data localmente
from demographic_data_analyzer import calculate_demographic_data

# Executa a função e imprime os resultados formatados
results = calculate_demographic_data()

print("Resultados da Análise Demográfica:")
for key, value in results.items():
    print(f"- {key.replace('_', ' ').capitalize()}: {value}")

