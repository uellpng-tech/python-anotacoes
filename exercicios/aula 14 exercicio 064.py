print ('CONDIÇÃO DE PARADA = 999')
n = 0
c = 0
s = 0
while n !=999:
    n = int (input ('Digite um número: '))
    s += n
    c += 1
print ('{} números digitados,{} soma de todos eles'.format(c-1,s-999))