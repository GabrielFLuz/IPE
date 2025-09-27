pali = input('Escreva uma palavra ').lower().replace(" ", "")
pali_inverso = pali.lower().replace(" ", "")[::-1]
print(pali_inverso)

if pali == pali_inverso:
    print('é um palíndromo')
else:
    print('não é palíndromo')