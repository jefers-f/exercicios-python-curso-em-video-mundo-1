from termcolor import colored
vel = int(input('Qual é a velocidade atual do carro? '))
if vel <= 80:
    print(colored('Tenha um bom dia, dirija com segurança!', 'green'))
else:
    print(colored('MULTADO! Você excedeu o limite de velocidade permitido, que é 80Km/h.', 'red'))
    print(colored('Você receberá 5 pontos na carteira e deverá pagar uma multa de ', 'red'),
          colored('R$280,00', 'yellow'))
