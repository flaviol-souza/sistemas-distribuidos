import requests

url = 'https://www.4devs.com.br/ferramentas_online.php'
header = {
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.4devs.com.br',
    'referer': 'https://www.4devs.com.br/gerador_de_pessoas',
}

param = 'acao=gerar_pessoa&sexo=I&pontuacao=S&idade=0&cep_estado=&txt_qtde=1&cep_cidade='

data = requests.post(url, headers=header, data=param).json()
for person in data:
    nome = (person['nome'])
    idade = (person['idade'])
    cpf = (person['cpf'])
    dataNac = (person['data_nasc'])
    sexo = (person['sexo'])
    print(f"Nome: {nome} \nIdade: {idade}\nCPF: {cpf}\nIdade: {idade}\nData de nascimento: {dataNac}\nSexo: {sexo}")