import math
co=float(input('Digite o cateto oposto: '))
ca=float(input('Digite o cateto adjacente: '))
h=(math.pow(co,2)) + (math.pow(ca,2))
print('O valor da hipotenusa é: {:.2f}'.format(math.sqrt(h)))