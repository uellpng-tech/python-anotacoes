n = int (input ('Acerte o número de 0 a 10 '))
if n == 3:
    print ('De primeira boaaaa')
s = 1
while n != 3:
    s += 1
    n = int (input('Tente de novo '))
    if n == 3 :
        print ('acertou!!!!!!!!!!!!! {} tentativas'.format(s))