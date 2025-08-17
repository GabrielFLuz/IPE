"""
Roteiro 01 - Formatação de Strings

Criando um programa simples que utilize o comando print() para exibir informações
de um perfil de usuário. 
"""
# criação de variaveis
nome = 'Gabriel' # Exemplo de string simples
idade = 25 # Exemplo de número inteiro
cidade = 'Valinhos' 
profissao = 'profissão' 
altura = 1.85 # Exemplo de número float

# Exibindo informações formatadas
print(f'Meu nome é {nome} ----- Moro em{cidade}.')  # Exemplo de f-string
print(nome, cidade, sep=' - ') # Exemplo de separador personalizado
# Exemplo de formatação de número inteiro com zeros à esquerda
print(f"Tenho {idade:05d} anos, porém ainda não sou formado, logo\nnão tenho {profissao}.")
# Exemplo de formatação de número float com uma casa decimal
print(f'Possuo {altura:1.1f}m de altura') 
print('--------------------------------------------------------------------')

# Interagindo com o usuário
print('Bom dia, qual seu nome?') 
nome = input() # Recebendo o nome do usuário
# Perguntando idade e cor favorita do usuário
print(f'Ola {nome}. Eu poderia saber qual sua idade e cor favorita?') 
print('--------------------------------------------------------------------')
idade1 = (int(input("Idade: "))) # Recebendo idade do usuário
cor = input("Cor: ") # Recebendo cor favorita do usuário
# Exibindo informações formatadas com f-string
print(f'UAU!!! {idade1} anos, que incrível, e quem imaginaria\nque você gostaria de {cor}') 
print('--------------------------------------------------------------------')

# Exibindo informações com format

# Exemplo de formatação com placeholders
texto = 'Meu nome é {} e tenho {} anos de idade. Minha cor favorita é {} e tenho {}m de altura' 
# Exibindo informações formatadas com o método format
print(texto.format(nome, idade, cor, altura)) 
# Exibindo informações formatadas com o método format com novos valores
print(texto.format('Ana', 30, 'azul', 1.65)) 

# Exemplo de formatação com placeholders nomeados
texto = 'Meu nome é {n} e tenho {i} anos de idade. Minha cor favorita é {c} e tenho {a}m de altura'
# Exibindo informações formatadas com o método format com placeholders nomeados
print(texto.format(n=nome, i=idade, c=cor, a=altura)) 

# Exibindo informações com separador personalizado e finalização de linha personalizada
print(idade, nome, altura, cor, end='FIM\n', sep='||') 

# Exibindo uma tabela de preços
print('Maçã\t\tR$ 1,00\nBanana\t\tR$ 2,00\nLaranja\t\tR$ 3,00') # Exemplo de tabulação para criar uma tabela simples
print('--------------------------------------------------------------------')
