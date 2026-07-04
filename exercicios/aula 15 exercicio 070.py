print ('\033[1;31;43mMERCADO 3 IRMÕES\033[m')
p1000 = 0
t = 0
pr = 0
me = 0
c = 'y'
co = 0
while c != 'N':
    p = str (input('Nome do produto: '))
    pr = int (input('Preço: '))
    co +=1
    t += pr
    if pr > 1000:
        p1000 += 1
    if co == 1:
        me = pr
    else:
        if pr < me:
            me = pr
    c = str (input('deseja continuar S/N: ')).upper()
    if c == 'N':
        break
print (f'{t} total gasto,{p1000} produtoa acima de 1000, {me} mais barato')