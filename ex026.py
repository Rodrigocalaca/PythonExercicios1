string = str(input('Digite uma frase: ')).upper()
print(string.count('A'))
print('Primeira ocorrencia da letra A acontece em {} e a última acontece em {}'.format(string.find('A') + 1,string.rfind('A')+1))
