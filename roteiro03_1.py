l1 = int(input('diga a medida do angulo interno em graus '))
l2 = int(input('diga a medida do angulo interno em graus '))
l3 = int(input('diga a medida do angulo interno em graus '))

if l1 == l2 and l2 == l3 and l1 == l3:
    print('É equilatero')
elif l1 == l2 and l1 != l3 or l1 == l3 and l1 != l2 or l2 == l3 and l2 != l1:
    print('é isoceles')
else:
    print('é escaleno')
    
