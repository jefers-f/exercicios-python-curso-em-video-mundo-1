frase = input('Digite uma frase: ').upper().strip()
n1 = frase.count('A')
n2 = frase.find('A')
n3 = frase.rfind('A')
print('Quantas vezes aparece a letra A? {}'.format(n1))
print('Em que posição ela aparece a primeira vez? {}'.format(n2))
print('Em que posição ela aparece pela ultima vez? {}'.format(n3))
