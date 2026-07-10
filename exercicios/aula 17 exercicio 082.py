l = []
impar = []
par = []
while True:
    n = int(input("Digite um número: "))
    c = input("Deseja continuar S/N: ").upper()
    l.append(n)
    if c == "N":
        break
    
for c in range (0, len(l)):
    if l[c]%2 == 0:
        par.append(l[c])
    else:
        impar.append(l[c])

print(f"lista completa {l}\n lista com números pares {par} \n lista com números ímpares {impar}")
