# Crie um programa para o pc jogar Jokenpô com você.

from time import sleep


def escolha():
    """
    -> Deve-se usar as variáveis 'pc' e 'user' no codigo global
    :return: pc, user
    """
    global pc
    global user
    from random import choice
    pc = ('tesoura', 'papel', 'pedra')
    pc = choice(pc)
    print('PEDRA *** PAPEL *** TESOURA ')
    user = input('\nFaça sua escolha: ').strip().lower()
    while user != 'pedra' and user != 'papel' and user != 'tesoura':
        user = input(f'{red}Opção inválida!{noColor}'
                     f'\nFaça sua escolha novamente: ').strip().lower()


def verifywin(item1, item2):
    """
    -> Verifica quem venceu.
    :param item1: máquina
    :param item2: jogador
    :return: 'Loss' se item1 vencer, 'Win' se item1 perder ou 'Draw' se empatar
    """

    if item1 == 'tesoura' and item2 == 'papel':
        return 'Loss'
    elif item1 == 'papel' and item2 == 'pedra':
        return 'Loss'
    elif item1 == 'pedra' and item2 == 'tesoura':
        return 'Loss'
    elif item2 == 'tesoura' and item1 == 'papel':
        return 'Win'
    elif item2 == 'papel' and item1 == 'pedra':
        return 'Win'
    elif item2 == 'pedra' and item1 == 'tesoura':
        return 'Win'
    else:
        return 'Draw'


def continuar():
    from os import system, name
    resposta = input('\nDeseja jogar novamente? <S>/<N> ').strip().upper()

    while resposta != 'N' and resposta != 'S':
        print(f'{red}Opção inválida!{noColor}')
        resposta = input('\nDeseja jogar novamente? <S>/<N> ').strip().upper()
    if resposta == 'N':
        system('cls' if name == 'nt' else 'clear')
        return False
    elif resposta == 'S':
        system('cls' if name == 'nt' else 'clear')
        return True


def encerramento(wins, losses, draw):
    print('=' * 9, f'{"Jogo encerrado":^6}', ('=' * 9))
    print(f'{green}Vitórias: \t{wins}'
          f'\n{red}Derrotas: \t{losses}'
          f'\n{blue}Empates: \t{draw}{noColor}')
    print('=' * 9, f'{"Volte sempre!":^6}', ('=' * 9))


red = '\033[31m'
green = '\033[32m'
blue = '\033[34m'
yellow = '\033[33m'
noColor = '\033[m'

perdas = 0
vitorias = 0
empates = 0
pc = ''
user = ''

print('=' * 9, f'{"JOKENPÔ":^6}', ('=' * 9))

while True:
    escolha()

    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PÔ!')
    sleep(0.5)
    print(f'\nVocê escolheu {user.upper()}'
          f'\nO computador escolheu {pc.upper()}')

    resultado = verifywin(pc, user)
    if resultado == "Win":
        print(f'{green}Você venceu!{noColor}')
        vitorias += 1
    elif resultado == 'Loss':
        print(f'{red}Você perdeu...{noColor}')
        perdas += 1
    elif resultado == 'Draw':
        print(f'{blue}Empatou{noColor}')
        empates += 1

    ans = continuar()
    if not ans:
        break
    else:
        continue

encerramento(vitorias, perdas, empates)
