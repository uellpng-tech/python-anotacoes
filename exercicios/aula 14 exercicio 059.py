n1 = int (input('digite um número '))
n2 = int (input('digite outro número '))
maior = 0
menor = 0
m = int (input(''' 1/ somar 
 2/ multiplicar
 3/ maior
 4/ novos números
 5/ sair '''))
n = 0
while n == 0:
    if m == 1:
        print ('A soma de {} com {} é {}'.format(n1,n2,n1+n2))
        n += 1
    elif m == 2:
        print ('{} multiplicado por {} é {}'.format(n1,n2,n1*n2))
        n += 1
    elif m == 3:
        menor = n1
        menor = n2
        if n1 >= n2:
            maior = n1
            menor = n2
        if n2 >= n1:
            maior = n2
            menor = n1
        print ('{} é maior que {}'.format(maior,menor))
        n += 1
    elif m == 4:
        n1 = int (input('digite um número '))
        n2 = int (input('digite outro número '))
        m = int (input(''' 1/ somar 
 2/ multiplicar
 3/ maior
 4/ novos números
 5/ sair '''))
        n = 0
    elif m == 5:
        print ('desconectado do programa')
        n += 1