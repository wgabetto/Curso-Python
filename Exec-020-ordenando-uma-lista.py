import random
nomes = []
print('Digite o nome de quatro alunos.')
for i in range(4):
    nome = input('nome do aluno: ')
    nomes.append(nome)
random.shuffle(nomes)
print('A ordem de apresentação será:')
print(nomes)