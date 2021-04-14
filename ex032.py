from datetime import date
ano = int(input('Que ano quer analisar: \nOBS: Coloque 0 caso queria verificar o ano atual '))
if ano == 0:
    ano = date.today().year
    print(ano)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto!')