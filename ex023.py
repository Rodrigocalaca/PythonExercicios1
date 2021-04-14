n = int(input('Digite um número: '))
u = n // 1 % 10
c = n // 10 % 10
d = n // 100 % 10
m = n // 1000 % 10
print('A unidade, centena, dezena e milhar são, respectivamente: {},{},{},{}'.format(u,c,d,m))