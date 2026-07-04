n = 0
c = 0
s = 0
while n != 999:
    n = int(input('Digite um número (999 para): '))
    c += 1
    if n == 999:
        break
    s += n 
print (f'{c} tentativas, {s} soma entre eles')