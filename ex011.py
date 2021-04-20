lar = float(input('Qual a largura da parede em metros? '))
alt = float(input('Qual a altura da parede em metros? '))
a = lar * alt
tinta = a / 2
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m².'.format(lar, alt, a))
print('Para pintar essa parede, vocÊ precisará de {:.3f}l de tinta.'.format(tinta))
