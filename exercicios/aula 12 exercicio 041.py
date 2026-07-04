a = int (input ('Qual ano você nasceu? '))
c = int (2025-a)
if c < 8:
    print ('Você é muito novo')
elif c <= 9 and c < 14:
    print ('{} atleta mirim'.format (c))
elif c <= 14 and c < 19:
    print ('{} atleta infantil'.format (c))
elif c <= 19 and c < 20:
    print ('{} atleta junior'.format (c))
elif c <= 20 and c < 21:
    print ('{} atleta sênior'.format (c))
elif c > 21:
    print ('{} atleta master'.format (c))