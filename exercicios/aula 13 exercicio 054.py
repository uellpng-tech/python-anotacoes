for c in range (1,8):
    n = int (input('digite seu ano de nascimento '))
    n = 2025-n
    if n >= 17:
        print ('maior de idade {}'.format(n))
    else:
        print ('menor de idade {}'.format(n))