nome = 'Gabriel'
idade = 25
cidade = 'Valinhos'
profissao = 'profissão'
altura = 1.85

print(F'Meu nome é {nome}\n-------------------\nMoro em {cidade}.')
print(F"Tenho {idade:05d} anos, porém ainda não sou formado, logo\nnão tenho {profissao}.")
print(F'Possuo {altura:1.1f}m de altura')
print('--------------------------------------------------------------------')

print('Bom dia, qual seu nome?')
nome = input()
print(f'Ola {nome}. Eu poderia saber qual sua idade e cor favorita?')
print('--------------------------------------------------------------------')
idade1 = input(int)
cor = input()
print(f'UAU!!! {idade1} anos, que incrível, e quem imaginaria\nque você gostaria de {cor}')
print('--------------------------------------------------------------------')

print(idade, nome, altura, cor, sep='---', end=' FIM')