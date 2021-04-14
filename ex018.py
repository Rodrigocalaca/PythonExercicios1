import math
angulo=float(input('Qual o ângulo desejado: '))
sin=math.sin(math.radians(angulo))
cos=math.cos(math.radians(angulo))
tg=math.tan(math.radians(angulo))
print('O ângulo tem o seno {:.2f} o cos {:.2f} e a tangente {:.2f}'.format(sin,cos,tg))