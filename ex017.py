from math import hypot
cop = float(input('Qual o comprimento do cateto oposto? '))
cad = float(input('Qual o comprimento do cateto adjacente? '))
hip = hypot(cop, cad)
print('A hipotenusa irá medir {:.2f}'.format(hip))
