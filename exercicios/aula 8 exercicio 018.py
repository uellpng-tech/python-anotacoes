import math

angulo = float(input('Digite o ângulo que você deseja: '))
rad = math.radians(angulo)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

print(f'O ângulo de {angulo}° tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo}° tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {angulo}° tem a TANGENTE de {tangente:.2f}')