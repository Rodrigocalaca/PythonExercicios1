n1 = float(input('Digite o 1 segmento: '))
n2 = float(input('Digite o 2 segmento: '))
n3 = float(input('Digite o 3 segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 or n3 < n1 + n2:
    print('Esses segmentos podem formar um triângulo!')
else:
    print('Esses segmentos não podem formar um triângulo!')