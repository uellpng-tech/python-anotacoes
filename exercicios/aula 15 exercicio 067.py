n = int(input('Quer ver qual tabuada: '))
c = 0
while True:
    c += 1
    m = n*c
    print (f'{m}')
    if c == 10:
        n = int (input('Quer ver qua tabuada: '))
        c = 0
    if n < 0:
        break