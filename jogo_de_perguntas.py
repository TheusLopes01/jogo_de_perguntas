# Exercício - sistema de perguntas e respostas
import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
resposta1 = '2'
resposta2 = '0'
resposta3 = '1'
opcoes = '0', '1', '2', '3'
perguntas_corretas = 0


while True:
    # PERGUNTA 1
    print(f'Pergunta 1: {perguntas[0]['Pergunta']}\n')
    print('Opções: ')
    print('0)', perguntas[0]['Opções'][0])
    print('1)', perguntas[0]['Opções'][1])
    print('2)', perguntas[0]['Opções'][2])
    print('3)', perguntas[0]['Opções'][3])

    opcoes1 = input(f'Escolha uma opção: ')
    os.system('cls')

    if opcoes1 == resposta1:
        print('Acertou 👍')
        perguntas_corretas += 1

    elif opcoes1 not in opcoes:
        print('Digite alguma das alternativas')
    else:
        print(f'Errou 👎')

    # PERGUNTA 2
    print(f'Pergunta 2: {perguntas[1]['Pergunta']}\n')
    print('Opções: ')
    print('0)', perguntas[1]['Opções'][0])
    print('1)', perguntas[1]['Opções'][1])
    print('2)', perguntas[1]['Opções'][2])
    print('3)', perguntas[1]['Opções'][3])

    opcoes2 = input(f'Escolha uma opção: ')
    os.system('cls')

    if opcoes2 == resposta2:
        print('Acertou 👍')
        perguntas_corretas += 1
    elif opcoes2 not in opcoes:
        print('Digite alguma das alternativas')
    else:
        print(f'Errou 👎')

    # PERGUNTA 3
    print(f'Pergunta 3: {perguntas[2]['Pergunta']}\n')
    print('Opções: ')
    print('0)', perguntas[2]['Opções'][0])
    print('1)', perguntas[2]['Opções'][1])
    print('2)', perguntas[2]['Opções'][2])
    print('3)', perguntas[2]['Opções'][3])

    opcoes3 = input(f'Escolha uma opção: ')
    os.system('cls')
    if opcoes3 == resposta3:
        print('Acertou 👍')
        perguntas_corretas += 1
    elif opcoes3 not in opcoes:
        print('Digite alguma das alternativas')
        os.system('cls')
        print('Você não digitou nenhuma alternativa nas 3 perguntas')
    else:
        print(f'Errou 👎')
        os.system('cls')
    print(f'Você acertou {perguntas_corretas}\nde 3 perguntas')
    break