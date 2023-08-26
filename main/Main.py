import json
import pandas as pd
import requests
import random

#Função para retornar os dados dos usuários através dos seus ID's
def get_user(id):
  response = requests.get(f'{sdw2023_api_url}/users/{id}')
  return response.json() if response.status_code == 200 else None

#URL da API 'desenvolvida para a Santander Dev Week 2023'
sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'

#Extração dos ID's presentes no arquivo .csv
df = pd.read_csv('BCS2023.csv')
user_ids = df['UserID'].tolist()
print(f"Users Id's: {user_ids}")

users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))

#Frases que serão usadas para atualizar a lista de news dos clientes
phrases = ["Prepare-se para o futuro: invista hoje!", "Seu dinheiro merece crescer: invista agora.", 
           "Realize sonhos: invista seu dinheiro.", "Não adie mais, comece a investir hoje!", 
           "Coloque seu dinheiro para render: invista!", "Investir é o segredo do crescimento financeiro"]

#Adiciona as frases e um ícone a cada usuário
for user in users:
  news = phrases[random.randrange(len(phrases))]
  print(news)
  user['news'].append({
      "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
      "description": news
  })
  
print(json.dumps(users, indent=2))