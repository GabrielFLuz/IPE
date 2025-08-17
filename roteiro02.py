# Roteiro 02 - Python Básico

print('Decompondo um "ncdu"\n\n-----------------------------------\n') # Exemplo de decomposição de um número
numero = int(526) # Atribuindo um número inteiro à variável numero

unidade = numero % 10 # Calculando a unidade do número decompondo-o pelo resto da divisão por 10
print(unidade) # Exibindo a unidade ao usuário

dezena = (numero // 10) % 10  # Calculando a dezena do número decompondo-o pela divisão inteira por 10 e pelo resto da divisão por 10 e sem exibir a parte fracionária
print(dezena) # Exibindo a dezena ao usuário

centena = numero // 100 # Calculando a centena do número decompondo-o pela divisão inteira por 100 sem exibir a parte fracionária
print(centena) # Exibindo a centena ao usuário

print() 
print(centena, dezena, unidade, end="\n\n") # Exibindo a centena, dezena e unidade com uma quebra de linha no final

print("Calculando seu imc\n\n-----------------------------------------------------------\n") # Exemplo de cálculo do IMC (Índice de Massa Corporal)
altura = float(input('Qual sua altura?')) # Recebendo a altura do usuário
print()

peso = float(input('Seu peso?')) # Recebendo o peso do usuário

imc = peso / (altura**2) # Calculando o IMC dividindo o peso pela altura ao quadrado
print('Seu imc é', imc) # Exibindo o IMC ao usuário
print('----------------------------------------------------------------\n')

# Exemplo de conversão de decimal para binário
print('Convertendo binários entre 0 e 15\n')
print("----------------------------------------------------------------\n")

decimal = int(input('digite um número entre 0 e 15 ')) # Recebendo um número decimal do usuário
resultado = "" # Inicializando uma string vazia para armazenar o resultado da conversão
while decimal > 0: # Enquanto o número decimal for maior que zero
      resto = decimal % 2 # Calculando o resto da divisão do número decimal por 2
      resultado = str(resto) + resultado # Concatenando o resto à string resultado
      decimal = decimal // 2 # Atualizando o número decimal dividindo-o por 2 e descartando a parte fracionária
      
print('O número em binário é', resultado)  # Exibindo o resultado da conversão do número decimal para binário