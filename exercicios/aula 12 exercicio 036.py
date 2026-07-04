v = float (input ('Qual valos da casa? '))
s = float (input ('Qual seu sálario? '))
a = float (input ('Em quantos anos você ira pagar'))
print ('Só um segundo ')
s3 = float (s*0.30)
c = float (a*12)
rc = float  (v/c)
if s3 <= rc :
    print ('negado')
else:
    print ('aprovado')