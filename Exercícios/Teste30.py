from random import randint
from time import sleep
computador = randint(0, 5) #Faz o computador "PENSAR" em algum número aliatório entre 0 e 5 e mostrar na tela
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei? ')) #Faz o jogador adivinhar
print('Processando...')
sleep(3) # Faz com que o computador leve um tempo para processar antes de mostrar o resultado na tela.
#Condição composta com if e else
if jogador == computador:
    print('Parabéns! Você me venceu cassule!')
else:
    print('Ganhei! Eu pensei no número {} e não no número {}'.format(computador, jogador))