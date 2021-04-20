p = float(input('Qual o preço do produto? R$ '))
d = float(input('Qual será a % de desconto? '))
desc = d / 100
vd = p * desc
vp = p - vd
print('O produto que custava R${:.2f}, na promoção com desconto de {:.0f}% vai custar R${:.2f}'.format(p, d, vp))
