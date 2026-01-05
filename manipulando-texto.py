# frase = 'Kauan Medeiros Marins'
# print(frase[0:7:])
# print(len(frase))
# print(frase.count('a'))
# print(frase.find('Kauan'))
# print('Kauan' in frase)
# print(frase.capitalize())
# print(frase.title())
# print(frase.strip())
# print('-_-'.join(frase))
# print(frase.replace('Kauan', 'Ronaldinho'))

# nome = str(input('Digite seu nome completo se possível:')).strip
# maiuscolo = nome.upper()
# minusculo = nome.lower()
# nome_completo = len(nome_espaco) - nome.count(' ') ou nome_espaco = nome.replace(' ', '')
# letras_converte = nome.split()
# letras_primeiro = len(letras_converte[0])
# print('Seu nome em maiúscolo é {}'
#      '\nSeu nome em minúsculo é {}'
#      '\nEssa é a quantidade de letras do seu nome completo {}'
#      '\nEssa é a quantidade de letras do seu primeiro nome {}'
#      .format(maiuscolo, minusculo, nome_completo, letras_primeiro))

# n = int(input('Digite um numeros:'))
# u = n // 1 % 10
# d = n // 10 % 10
# c = n // 100 % 10
# m = n // 1000 % 10
# print('unidade:{}\ndezena:{}\ncentena:{}\nmilhar:{}'
#       .format(u, d, c, m,))

# cidade = str(input('Digite sua cidade:')).strip()
# print(cidade[:5].lower() == 'santo')

# nome = str(input('Digite seu nome completo:')).strip()
# print('Seu sobrenome tem Medeiros? {}'.format('Medeiros' in nome.title()))

# nome = str(input('Digite uma frase:')).strip().lower()
# print('A letra A aparece {} vezes na frase.'.format(nome.count('a')))
# print('A primeira letra A aparece na posição {}'.format(nome.find('a')+1))
# print('A ultima letra a parece na posição {}'.format(nome.rfind('a')+1))

# nome = str(input('Digite seu nome completo:')).strip().split()
# print('Seu primeiro nome é {}'.format(nome[0]))
# print('Seu ultimo nome é {}'.format(nome[-1]))