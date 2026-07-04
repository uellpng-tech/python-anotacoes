a = int (input ('Qual altura da sua parede? '))
l = int (input ('Qual largura da sua parede? '))
area = (a*l)
print ('para poder pintar a parede precisa de {} litros de tinta'.format (area//2))