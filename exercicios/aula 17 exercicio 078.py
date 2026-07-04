num = []
maior = 0
menor = 0
for c in range(0, 5):
    num.append(int(input(f'Digite um número para a posição {c} ')))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
        if maior < menor:
            menor = maior

print('maior valor ', maior,f'posição {num.index(maior)}', '\nmenor valor', menor, f'posição {num.index(menor)}')