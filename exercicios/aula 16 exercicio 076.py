listagem = ['jubileu',2.50,'quanzas',500,'cogumelo',1.50,'todinho', 9.00]

c = 0
co = 0
fim = 1

while c != 4:
    c += 1
    print (listagem[co], end=".................................R$  ")
    print (listagem[fim])
    co += 2
    fim += 2