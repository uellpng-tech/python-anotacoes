exp = input("Digite uma expressão: ")
l = list(exp)
paren = 0
for c in range (0, len(l)):
    if "(" in l[c]:
        paren += 1
    elif ")" in l[c]:
        paren += 1
if paren % 2 == 0:
    print("parênteses corretos")
else:
    print("parênteses incorretos")