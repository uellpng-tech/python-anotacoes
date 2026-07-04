n1 = int (input("Digite um número: "))
n2 = int (input("Digite um número: "))
n3 = int (input("Digite um número: "))
n4 = int (input("Digite um número: "))
t = [n1,n2,n3,n4]
print (f"o valor 9 apareceu {(t.count(9))}")

print (f"a posição do número 3 é {t.index(3)+1}")

print ("pares:", end=" ")
for c in t:
    if c % 2 == 0:
        print (c , end=" ")