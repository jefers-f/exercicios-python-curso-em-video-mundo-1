d = float(input('Digite uma distância em metros: '))
q = d / 1000
h = d / 100
dc = d / 10
dec = d * 10
c = d * 100
mm = d * 1000
print('A medida de {} metros corresponde a: '.format(d))
print('{}km'.format(q))
print('{}hm'.format(h))
print('{}dam'.format(dc))
print('{}dm'.format(dec))
print('{}cm'.format(c))
print('{}mm'.format(mm))
