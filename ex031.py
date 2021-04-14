k = float(input('Digite o preço da viagem em Km: '))
if k>200:
    preço = k*0.45
    print('O preço da viagem será: R${:.2f}'.format(preço))
else:
    preço = k*0.5
    print('O preço da viagem será: R${:.2F}'.format(preço))