valores = []

while True:
    v = int(input("Digite um valor: "))
    valores.append(v)

    if valores.count(v) == 2:
        valores.remove(v)

    sn = str(input("deseja continuar S/N: ")).upper()

    if sn == "N":
       valores.sort()
       print(valores)
       break

    if sn != "S" and sn != "N":
        print("apenas S ou N")