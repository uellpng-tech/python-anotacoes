palavras = ["sol","teclado","horizonte","cafe","algoritmo","janela","nuvem","estrada","livro","farol","psst"]

for p in palavras:
    print(f"\nNa palavra {p} temos", end=" ")
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=" ")