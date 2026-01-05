import random

# numero = int(input('Tente adivinhar o numero de 0 até 5:'))
# n = [0, 1, 2, 3, 4, 5]
# adivinha = random.choice(n)
# if numero == adivinha:
#    print('Parabéns, você acerto')
# else:
#    print('Você ERROU!')
# print('O número certo era {}'.format(adivinha))


# velocidade = int(input('Digite a velocidade do seu veículo:'))
# multa = velocidade - 80
# total = multa * 7
# if velocidade >= 80:
#    print('Você foi multado!')
#
#    print(f'Você estava {multa}km/h acima da velocidade permitida, Sua multa é R${total} reais')
# else:
#    print('Sua velocidade esta aceitável, Continue assim :)')

# n = int(input('Digite um número e descubra se ele é ímpar ou par:'))
# if n % 2 == 0:
#    print(f'O número {n} é Par')
# else:
#    print(f'O número {n} é ímpar')

# d = float(input('Digite sua distancia da viagem:'))
# if d <= 200:
#    r = d * 0.50
#    print(f'Sua viagem vai custar R${r} :(')
# else:
#    r = d * 0.45
#    print(f'Sua viagem vai custar R${r} :)')

ano = int(input('Digite um ano e descubra se é bissexto:'))
b = ano / 4 or 400 or 100
if b != int:
    print(f'O ano {ano} é Bissexto')
else:
    print(f'Seu ano {ano} não é Bissexto')
