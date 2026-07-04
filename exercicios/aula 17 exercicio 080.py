lista = []

while True:
    v = int(input("Digite um valor: "))
    c = input("Deseja contiuar S/N: ").upper()
    lista.append(v)

    if c == "N":
        print("Números de valores adicionados:",len(lista))
        lista.sort(reverse=True)
        if 5 in lista:
            print(lista)
            print("O valor 5 foi digitado e está na lista")
        else:
            print(lista)
        break

    if c != "S" and c != "N":
        print("Apenas S ou N")

