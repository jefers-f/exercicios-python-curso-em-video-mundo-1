import random
import time
num = int(input('Em qual numero eu pensei? '))  #Faz o jogador tentar adivinhar
n1 = random.randint(0, 5) #faz o computador pensar em um numero
print('Processando...')
time.sleep(2)
if num == n1:
    print('Você me venceu! Eu pensei no numero {}!'.format(num))
else:
    print('hahaha você perdeu! Eu pensei no numero {}'.format(num))