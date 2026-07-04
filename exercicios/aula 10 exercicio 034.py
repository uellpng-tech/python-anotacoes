s = int (input('Qual seu sálario? '))
if s>=(1250):
    c = s*0.10
    print ('Aumento de 10% agora seu sálario é {}'.format(c+s))
else:
    c2 = s*0.15
    print ('Aumento de 15% agora seu sálario é {}'.format(c2+s))