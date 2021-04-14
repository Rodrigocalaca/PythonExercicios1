from random import randint
n = randint(0,5)
print('-=-'*18)
n1 = int(input('Escolha um número: '))
print('-=-'*18)
if n1 == n:
    print('Parabéns você acertou!!!')
    print('-=-' * 18)
else:
    print('HAHA fraquinho')
    print('-=-' * 18)