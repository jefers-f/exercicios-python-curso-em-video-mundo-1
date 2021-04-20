import random
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do seguno aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
lista = [a1, a2, a3, a4]
ordem = random.sample(lista, 4)
print('A ordem de apresentação do trabalho será {}'.format(ordem))

