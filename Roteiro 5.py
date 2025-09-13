n = int(input('Por favor, insira um número inteiro. '))
r = 0
for s in range(n+1):
    r += s
print(r)

#Ampliação do desafio

np = int(input('Insira um numero primo '))
ri = True
for nr in range(2, np):
    if np%nr==0:
        ri = False
        break
if ri:
    print(f'É primo')
else:
    print('Não é primo')