import random
n = [random.randint(1, 69) for _ in range(5)]
t = (n)
print (t)

if t[0] > t[1] and t[2] and t[3] and t[4]:
    maior = t[0]
elif t[0] < t[1] and t[2] and t[3] and t[4]:
    menor = t[0]

if t[1] > t[0] and t[2] and t[3] and t[4]:
    maior = t[1]
elif t[1] < t[0] and t[2] and t[3] and t[4]:
    menor = t[1]

if t[2] > t[1] and t[0] and t[3] and t[4]:
    maior = t[2]
elif t[2] < t[1] and t[0] and t[3] and t[4]:
    menor = t[2]

if t[3] > t[1] and t[2] and t[0] and t[4]:
    maior = t[3]
elif t[3] < t[1] and t[2] and t[0] and t[4]:
    menor = t[3]

if t[4] > t[1] and t[2] and t[3] and t[0]:
    maior = t[4]
elif t[4] < t[1] and t[2] and t[3] and t[0]:
    menor = t[4]

print (f"maior {maior} menor {menor}")