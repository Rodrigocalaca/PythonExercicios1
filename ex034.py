salario = float(input('Digite o valor do salário: '))
if salario<=1250:
    salario = salario * 1.15
else:
    salario *= 1.10
print('O valor do novo salário após o reajuste é de: {}'.format(salario))