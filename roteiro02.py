print('Decompondo um "ncdu"\n\n-----------------------------------\n')
numero = int(526)

unidade = numero % 10
print(unidade)

dezena = (numero // 10) % 10 
print(dezena)

centena = numero // 100
print(centena)

print()
print(centena, dezena, unidade, end="\n")

print("Calculando seu imcu\n-----------------------------------------------------------\n")
altura = float(input('Qual sua altura?'))
print()

peso = float(input('Seu peso?'))

imc = peso / (altura**2)
print('Seu imc é', imc)
print('----------------------------------------------------------------\n')
print('Convertendo binários entre 0 e 15\n')
print("----------------------------------------------------------------\n")

decimal = int(input('digite um número entre 1 e 15'))
binario = decimal 
