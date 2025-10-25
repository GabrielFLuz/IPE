from random import randint
from faker import Faker
from math import sqrt as raiz

fake = Faker('pt_BR')

def gerar_dados_usuario():
    nome = fake.name()
    endereco = fake.address().replace("\n", ", ")
    telefone = fake.phone_number()
    return nome, endereco, telefone

agenda = {}

def adicionar_usuario_agenda():
    nome, endereco, telefone = gerar_dados_usuario()
    agenda[nome] = {
        'email': fake.email(),
        'endereco': endereco,
        'telefone': telefone
    }

def laco_adicionar_usuarios(n):
    for _ in range(n):
        adicionar_usuario_agenda()

def gerar_numero_aleatorio(inicio, fim):
    return randint(inicio, fim)

def media_geometrica(x, y):
    produto = x * y
    media = raiz(produto)
    return media

def resgistro_de_pessoas():
    pessoas = []
    for _ in range(10):
        nome, endereco, telefone = gerar_dados_usuario()
        pessoas.append({
            'nome': nome,
            'telefone': telefone,
            'endereco': endereco,
            'email': fake.email(),
            'notas': (gerar_numero_aleatorio(0, 2), gerar_numero_aleatorio(0, 2)), #  duas tupla como duas notas aleatórias
            'media_geometrica': media_geometrica(gerar_numero_aleatorio(1, 10), gerar_numero_aleatorio(1, 10))
        })
    return pessoas
        
# Adiciona 10 usuários à agenda
laco_adicionar_usuarios(10)
print("\nRegistros de pessoas com detalhes:")

pessoas = resgistro_de_pessoas()
for pessoa in sorted(pessoas, key=lambda x: x['nome']):
    print(f"Nome: {pessoa['nome']}")
    print(f"Endereço: {pessoa['endereco']}")
    print(f"E-mail: {pessoa['email']}")
    print(f"Notas: {pessoa['notas']}")
    print(f"Média Geométrica das notas: {pessoa['media_geometrica']:.2f}")
    print("-" * 40)