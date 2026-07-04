n1 = int (input ('digite um número '))
n2 = int (input ('digite outro número '))
n3 = int (input ('último número '))
c = (n1+n2+n3)
if c == 180:
    print ('forma um triângulo')
else:
    print ('não forma um triângulo')
if n1 == n2 == n3:
    print ('triângulo Equilátero')
elif n1 == n2 or n2 == n3 or n1 == n3:
    print ('triângulo isósceles')
else:
    print ('triângulo escaleno')