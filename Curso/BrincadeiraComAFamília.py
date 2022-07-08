'''OS NOMES ENVOLVIDO NO GAME SÃO: JOÃO, FILIPE, ANDREZA E NÍCOLAS'''

from random import randint
from time import sleep
n = input('FAAAAALA FAMILÍA OLIVEIRA, QUAL SEU NOME?? ').upper()


if n == 'JOAO':
    print('AH, DENTIN, TU AQUI TÔ LIGADO!!')
elif n == 'FILIPE':
    print('PAIZÃO, REI DA CASA E DEV MAIS LINDO!!!')
elif n == 'ANDREZA':
    print('SEEI! A PRINCESA DA CASA')
elif n == 'NICOLAS':
    print('FAAALA NINICO, TUDO BOM? MOLEQUE MAIS FORTE DA TERRA')
else:
    print('OPAAAA! VOCÊ NÉ DA FAMILIA NÃO MAS NÃO TEM PROBLEMA, VOU TE GANHAR TAMBEM!! HAHA')
computador = randint(0,5)
sleep(2)
print('vou pensar em um número de 1 até 5, tente advinhar...')
sleep(2)
jogador = int(input('Qual número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABÉNS!!! Você me venceu, o numero que eu pensei foi {}!'.format(computador))
else:
    print('EU SOU MILHOR, GANHEI!!!. Você digitou {} e eu pensei em {}!!'.format(jogador, computador))