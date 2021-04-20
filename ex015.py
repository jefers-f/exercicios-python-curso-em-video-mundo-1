da = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos KM foram rodados? '))
ca = da * 60
ckm = km * 0.15
vp = ca + ckm
print('O total a pagar pelo aluguel do veículo é de R${:.2f}'.format(vp))
