v = int (input ('digite uma velocidade '))
if v<= (80):
    print ('continui assim!')
else:
    print (input('você foi multado por ultrapassar o limite de velocidade, sua multa deu {}'.format ((v-80)*7)))