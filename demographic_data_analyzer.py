import pandas as pd

def calculate_demographic_data():
    # Lê o conjunto de dados 'adult.csv' usando a biblioteca pandas
    df = pd.read_csv('adult.csv')

    # Pergunta 1: Quantas pessoas de cada raça estão representadas neste conjunto de dados?
    # Usamos value_counts() para contar as ocorrências de cada categoria na coluna 'race'
    race_count = df['race'].value_counts()

    # Pergunta 2: Qual a idade média dos homens?
    # Filtramos o DataFrame para incluir apenas homens ('Sex' == 'Male')
    men_age = df[df['sex'] == 'Male']['age']
    # Calculamos a média e arredondamos para uma casa decimal
    average_age_men = round(men_age.mean(), 1)

    # Pergunta 3: Qual a porcentagem de pessoas que têm um Bacharelado (Bachelors)?
    # Contamos o total de pessoas e o total com 'Bachelors'
    total_people = len(df)
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    # Calculamos o percentual e arredondamos para uma casa decimal
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)

    # Pergunta 4, 5, 7, 8, 9 envolvem pessoas com renda >50K e <=50K
    # Criamos máscaras booleanas para facilitar a filtragem
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education # A negação da máscara anterior
    earns_more = df['salary'] == '>50K'

    # Pergunta 4: Qual a porcentagem de pessoas com educação avançada que ganham >50K?
    hi_edu_rich_count = df[higher_education & earns_more].shape[0]
    percentage_hi_edu_rich = round((hi_edu_rich_count / df[higher_education].shape[0]) * 100, 1)

    # Pergunta 5: Qual a porcentagem de pessoas sem educação avançada que ganham >50K?
    low_edu_rich_count = df[lower_education & earns_more].shape[0]
    percentage_low_edu_rich = round((low_edu_rich_count / df[lower_education].shape[0]) * 100, 1)

    # Pergunta 6: Qual o número mínimo de horas que uma pessoa trabalha por semana?
    min_work_hours = df['hours-per-week'].min()

    # Pergunta 7: Qual a porcentagem de pessoas que trabalham o mínimo de horas por semana E ganham >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]
    rich_percentage_min_workers = round((df[
        (df['hours-per-week'] == min_work_hours) & earns_more
    ].shape[0] / num_min_workers) * 100, 1)

    # Pergunta 8: País com a maior porcentagem de pessoas ganhando >50K
    # Agrupamos por 'native-country' e contamos os ricos e o total de pessoas em cada país
    country_counts = df['native-country'].value_counts()
    rich_per_country = df[earns_more]['native-country'].value_counts()
    # Calculamos a porcentagem para cada país e encontramos o país com a maior porcentagem
    highest_earning_country = (rich_per_country / country_counts * 100).idxmax()
    highest_earning_country_percentage = round((rich_per_country / country_counts * 100).max(), 1)

    # Pergunta 9: Ocupação mais popular para quem ganha >50K na Índia
    # Filtramos para pessoas da Índia que ganham >50K
    india_rich = df[(df['native-country'] == 'India') & earns_more]
    # Encontramos a ocupação que aparece com mais frequência
    top_occupation = india_rich['occupation'].mode()[0] # .mode() retorna uma série, [0] pega o primeiro valor

    # Dicionário de resultados conforme especificado pelo freeCodeCamp
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': percentage_hi_edu_rich,
        'lower_education_rich': percentage_low_edu_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage_min_workers,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_occupation': top_occupation
    }

