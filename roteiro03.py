import datetime
print('Insira sua idade de nascimento')
nd = int(input('Insira o dia '))
nm = int(input('Insira o mes '))
na = int(input('Insira o ano '))

if nd <= 30 and nm <= 8 and na <= 2007:
    print('Tem permissão')
else: 
    print('Não tem permissão')