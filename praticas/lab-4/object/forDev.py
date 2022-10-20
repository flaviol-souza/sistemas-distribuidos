from calendar import c
import requests
from cacheout import Cache

class Person:
    def __init__(self, name, age, document, birthday, sex):
        self.name = name
        self.age = age
        self.document = document
        self.birthday = birthday
        self.sex = sex

    def __str__(self):
        return f'Person name is {self.name} and age is {self.age}'

cache = Cache(maxsize=256)
url = 'https://www.4devs.com.br/ferramentas_online.php'
header = {
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.4devs.com.br',
    'referer': 'https://www.4devs.com.br/gerador_de_pessoas',
}

param = 'acao=gerar_pessoa&sexo=I&pontuacao=S&idade=0&cep_estado=&txt_qtde=1&cep_cidade='

id=1
data = requests.post(url, headers=header, data=param).json()
for p in data:
    print(p)
    nome = (p['nome'])
    idade = (p['idade'])
    cpf = (p['cpf'])
    dataNac = (p['data_nasc'])
    sexo = (p['sexo'])
    person = Person(nome, idade, cpf, dataNac, sexo)
    cache.set(id, person)
    id+=1

for i in range(id):
    print(cache.get(i))