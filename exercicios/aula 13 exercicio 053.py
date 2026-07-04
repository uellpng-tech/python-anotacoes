f = str (input('digite uma frase '))
s = f.split()
j = ''.join(s)
i = ''
for c in range(len(j) - 1, -1, -1):
    i += j[c]
if i == j:
    print ('palíndromo')
else:
    print ('não é um palíndromo')