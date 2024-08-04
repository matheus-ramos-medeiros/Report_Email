import csv 
from faker import Faker
import random
import datetime



# Inicializar o Faker

fake = Faker()
num_rows = 15000

# Lista de colunas
headers = ['Data' , 'Nome do Produto' , 'Quantidade' , 'Lucro']


# Funções ===============
def gerar_data(dias: int):
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=dias)
    return fake.date_between(start_date = start_date , end_date = end_date)

def gerar_nome_do_produto():
    produtos = ['Produto A' , 'Produto B' , 'Produto C' , 'Produto D']
    return random.choice(produtos)

def gerar_quantidade():
    return random.randint(1,100)

def gerar_valor_venda():
    return round(random.uniform(10.0 , 1000.0), 2)


# Criar Lista de linhas

data = []

for _ in range(num_rows):
    row = [
        gerar_data(720),
        gerar_nome_do_produto(),
        gerar_quantidade(),
        gerar_valor_venda()
    ]
    data.append(row)

# Escrever os dados em um CSV

with open('faker_users.csv' , 'w' , newline = '') as csv_file:
    writer = csv.writer(csv_file)

    # Escrever o nome das colunas
    writer.writerow(headers)

    # Passar os dados falsos
    writer.writerows(data)



