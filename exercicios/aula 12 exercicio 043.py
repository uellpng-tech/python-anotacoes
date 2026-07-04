a = float (input ('Qual sua altura? ') )
p = float (input('Qual seu peso? '))
c1 = float (a*a)
c = int (70/c1)
print (c)
if c <= 18.5:
    print ('abaixo do peso')
elif c >= 18.5 and c < 25.0:
    print ('peso ideal')
elif c >= 25.0 and c < 30.0:
    print ('sobrepeso')
elif c >= 30.0 and c < 40.0:
    print ('obesidade')
else:
    print ('obesidade mórbida')