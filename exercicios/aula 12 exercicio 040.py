n1 = float (input ('digite a primeira nota '))
n2 = float (input ('digite a segunda nota '))
c = float ((n1+n2)/2)
if c <= 5:
    print ('REPROVADO!!!')
elif c >= 5 and c <= 6.9:
    print ('RECUPERAÇÃO!!!')
elif c >= 7 and c == 7:
    print ('APROVADO!!!! continue assim')