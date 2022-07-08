from time import sleep
print('LIMITE DE VELOCIDADE: 100Km/h')
velocidade = float(input('Qual a velocidade? '))
print('ANALISANDO...')
sleep(2)
if velocidade > 100:
    print('MULTADO!! Você ultrapassou 100km/h.')
    multa = (velocidade - 100) * 7
    print('Sua velocidade é {}KM/H e sua multa equivale a R${:.2f}'.format(velocidade, multa))
print('Muito bom dia, dirija com segurança')