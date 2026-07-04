print ('\033[1;31;43mCAIXA ELETRÔNICO DE KWANZAS\033[m')
v = int (input('Qual valor você deseja sacar: '))
t = v
n = 50
tc = 0
while True:
    if t >= n:
        t -= n
        tc += 1
    else:
        if tc > 0:
            print (f'{tc} kwanzas de {n}')
        if n == 50:
            n = 20
        elif n == 20:
            n = 10
        elif n == 10:
            n = 1
        tc = 0
        if t == 0:
            break