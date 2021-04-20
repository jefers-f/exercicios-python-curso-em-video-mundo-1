sa = float(input('Qual o salário atual? R$'))
aum = float(input('Quantos % terá de aumento? '))
sn = sa + sa * (aum / 100)
print('Um funcionario que ganhava R${:.2f}, com aumento de {:.0f}%, passará a ganhar R${:.2f}'.format(sa, aum, sn))
