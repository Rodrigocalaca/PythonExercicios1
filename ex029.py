vel = float(input('Digite a velocidade do carro: '))
if vel >=80:
    multa = (vel-80)*7
    print('Multado, preço a ser pago: {}'.format(multa))
else:
    print('Nada de errado por aqui!')
