player = int (input('''escolha oque jogar
[pedra]=1
[papel]=2
[tesoura]=3
 '''))
import random
npc = random.randint (1,3)
print ('npc escolheu {}'.format (npc))
if player == 1 and npc == 3:
    print ('GANHOU!!!!!')
elif player == 2 and npc == 1:
    print ('GANHOU!!!!')
elif player == 3 and npc == 2:
    print ('GANHOU!!!!')
elif player == npc:
    print ('EMPATE')
else:
    print ('PERDEU')