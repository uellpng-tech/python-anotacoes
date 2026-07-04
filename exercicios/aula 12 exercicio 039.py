a = int (input('Em que ano você nasceu? '))
c = int (2025-a)
if c > 18:
    print ('já passou o tempo {} ano, de se alistar a forças armadas brasileiras'.format(c-18))
elif c < 18:
    print ('falta {} ano para se alistar as forças armadas brasileiras se prepare'.format(18-c))
elif c == 18:
    print ('va se alistar nas forças armadas brasileira dia 30 de junho')