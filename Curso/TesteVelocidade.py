v = int(input('Digite a velocidade: '))
print('velocidade detectada foi {}Km/h'.format(v))
if v >= 80:
    print('Velocidade maior que 80km/h, você será multado em ')
else:
    print('Você está dentro dos limites de velocidade.')
    print('Permaneça assim!!')