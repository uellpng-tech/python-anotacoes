m20 = 0
h = 0 
p18 = 0
p = 's'
while p != 'N':
    i = int (input('Qual sua idade: '))
    s = str (input('Qual seu sexo H/M: ')).upper()
    p = str (input('Deseja continuar S/N: ')).upper()
    if i > 18:
        p18 += 1
    if s == 'H':
        h += 1
    if s == 'M' and i < 20:
        m20 += 1
    if p == 'N':
        break
print (f'{p18} mais de 18 anos, {h} homens, {m20} mulheres menos de 20')