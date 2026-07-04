import random
print ('PAR OU ÍMPAR')
c = 0
s = 0
d = 1
while True:
    n = n = random.randint(0,99999999)
    e = int (input('Digite um número: '))
    pr = str (input ('P/I?')).upper().split()[0]
    s += (n+e)%2
    if s == 0 and pr == 'P':
        print('Vitória')
        c += 1
    if s != 0 and pr == 'I':
        print('Vitória')
        c +=1
    if s == 0  and pr == 'I':
        print ('Derrota')
        break
    if s != 0 and pr == 'P':
        print ('Derrota')
        break
print (f'Vitórias seguidas {c}')