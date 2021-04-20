import math
ang = float(input('Digite o ângulo que você deseja: '))
rad = math.radians(ang)
sen = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)
print('O angulo de {} tem o SENO de {:.2f}'.format(ang, sen))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(ang, cos))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))
