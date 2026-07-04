p = int (input('Primeiro termo: '))
r = int (input('Razão: '))
t = p
c = 1
mt = 10
while c < mt:
    t += r
    c += 1
    print (t)
cn = str (input('Deseja continuar S/N?: '))
if cn == 'S' or cn == 's':
    v = int (input('Quantas vezes: '))
    mt = mt+v
while c < mt:
    t += r
    c += 1
    print (t)