n = 0
c = 't'
co = 0
s = 0
m = 0
me = 0
while c != 'N':
    n = int (input('Digite um número: '))
    co += 1
    s += n
    if co == 1:
        m = me = n
    else:
        if n > m:
            m = n
        if n < me:
            me = n
    c = str (input('Deseja continuar S/N: ')).upper().strip()[0]
print ('{} média dos valores digitados, {} maior valor e menor valor {}'.format(s/co,m,me))