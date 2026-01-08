# custa_casa = float(input('Quanto que custa a casa? R$'))
# salario = float(input('Quanto que é seu salario? R$'))
# quantos_anos = int(input('Em quantos anos você vai pagar:'))
# exceder = salario * 0.30
# quantos_meses = 12 * quantos_anos
# valor_mensal = custa_casa / quantos_meses
# if valor_mensal <= exceder:
#    print('Você vai pagar \033[1;32mR${:.2f}\033[m mensalmente até concluir o pagamento da casa que é \033[1;32mR${'
#          ':.2f}\033[m'.format(valor_mensal, custa_casa))
# else:
#    print('Seu empréstimo foi negado.')

# num = int(input('Digite um número: '))
# print('''Escolha uma das bases para conversão:
#      [1] para Binário
#      [2] para Octal
#      [3] para hexadecimal''')
# opcao = int(input('Sua opção: '))
# if opcao == 1:
#    print(f'{num} Binário igual a {bin(num)[2:]}')
# elif opcao == 2:
#    print(f'{num} Octal é igual a {oct(num)[2:]}')
# elif opcao == 3:
#    print(f'{num} Hexadecimal é igual a {hex(num)[2:]}')
# else:
#    print('opção invalida! Tente novamente.')

# n1 = int(input('Digite o primeiro numero:'))
# n2 = int(input('Digite o segundo numero:'))
# if n1 > n2:
#    print('O primeiro valor é maior')
# elif n2 > n1:
#    print('O segundo valor é maior')
# else:
#    print('Os dois valores são iguais')

# from _datetime import date
# atual = date.today().year
# ano = int(input('Ano de nascimento:'))
# idade = date.today().year - ano
# print(f'Quem nasceu em {ano} tem {idade} anos em 2026')
# if idade == 18:
#    print('Você tem que se alistar imediatamente!')
# elif idade < 18:
#    alistado = 18 - idade
#    print(f'Você ainda não tem 18 anos. ainda faltam {alistado}')
#    anos = alistado + atual
#    print(f'Seu alistamento vai ser em {anos}')
# elif idade > 18:
#    alistado = idade - 18
#    print(f'Você deveria ter se alistado há {alistado} anos.')
#    anos = atual - alistado
#    print(f'Seu alistamento foi em {anos}')

# primeiro_nota = float(input('Primeiro nota:'))
# segundo_nota = float(input('Segundo nota:'))
# media = (primeiro_nota + segundo_nota) / 2
# print('Tirando {} e {} a media do aluno é de {:.1f}'.format(primeiro_nota, segundo_nota, media))
# if media >= 6:
#    print('O aluno está APROVADO.')
# elif media >= 5:
#    print('O aluno está de RECUPERAÇÃO.')
# elif media < 5:
#    print('O aluno está REPROVADO.')

# import datetime as dat
# ano_nascimento = int(input('Digite seu ano de nascimento:'))
# idade = dat.date.today().year - ano_nascimento
# print(f'O atleta tem {idade} anos.')
# if idade <= 9:
#    print('Classificação: MIRIM')
# elif idade <= 14:
#    print('Classificação: INFANTIL')
# elif idade <= 19:
#    print('Classificação: JÚNIOR')
# elif idade <= 25:
#    print('Classificação: SÊNIOR')
# else:
#    print('Classificação: MASTER')

# n1 = float(input('Primeiro segmento:'))
# n2 = float(input('Segundo segmento:'))
# n3 = float(input('Terceiro segmento:'))
# if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
#    print('Os segmentos acima podem formar um triangulo!')
#    if n1 == n2 == n3:
#        print('Equilátero')
#    elif n1 != n2 != n3 != n1:
#        print('Escaleno')
#    else:
#        print('Isósceles')
# else:
#    print('Os segmentos acima não podem formar um triangulo!')

# peso = float(input('Qual seu peso? '))
# altura = float(input('Qual sua altura? '))
# imc = peso / (altura ** 2)
# print('O imc dessa pessoa é {:.1f}'.format(imc))
##    print('Você está abaixo do peso normal')
# elif imc < 25:
#    print('PARABÉNS, Você está na faixa de peso normal')
# elif imc < 30:
#    print('Você está em Sobrepeso')
# elif imc < 40:
#    print('Você está em Obesidade!')
# else:
#    print('Você está em Obesidade mórbida, cuidado')

