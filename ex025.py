nome = input('Qual é o seu nome completo? ')
n1 = nome.upper()
n2 = 'Sim' if 'SILVA' in n1 else 'Não'
print('Seu nome tem Silva? {}'.format(n2))