p = float (input ('Qual valor a ser pago? '))
f = str (input (''''Qual forma de pagamento?
[ 1 ] cartão 
[ 2 ] dinheiro  '''))
if f == ('1'):
    f1 = str (input ('''quantas vezes?
[ 2x ]
[ 3x ]
[mais]'''))
    if f1 == ('2x'):
        print ('{}, preço normal'.format (p))
    elif f1 == ('3x'):
        print ('{}, 20% de juros'.format ((p*0.20)+p))
elif f == ('2'):
    print ('{}, 10% de desconto'.format((p*0.10)-p))