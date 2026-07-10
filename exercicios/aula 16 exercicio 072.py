ne = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
p = int (input('Escreva quantos jogos você já zerou de 0 a 20'))

if p > 20 or p < 0:
    print('hahaha engraçadinho de 0 a 20')
    p = int (input('Escreva quantos jogos você já zerou de 0 a 20'))
else:
    print(f'Oloko {ne[p]} parabéns!')