import random
nomes = []
for i in range(4):
    nome = input('digite o nome do aluno: ')
    nomes.append(nome)
sorteado = random.choice(nomes)
print('O aluno sorteado foi {}.'.format(sorteado))