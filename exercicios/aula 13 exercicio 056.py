sd = 0
mdi = 0
mih = 0
nv = ''
m2 = 0
for p in range (1,5):
    n = str (input('nome da {} pessoa '.format(p))) 
    i = int (input('idade da {} pessoa '.format(p)))
    s = str (input('''sexo [h] homem [m] mulher '''))
    sd += i
    if p == 1  and s == 'h':
        mih = i
        nv = n
    if s in 'h' and i > mdi:
        mdi = i
        nv = n
    if s in 'm' and i < 20:
        m2 += 1
mdi = sd/4
print ('média de idade {}'.format(i/4))
print ('homem mais velho {}'.format(nv))
print ('{} mulheres tem menos de 20'.format(m2))