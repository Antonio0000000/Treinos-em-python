# Crie um programa para o pc jogar Jokenpô com você.

from time import sleep
from random import choice
from os import system, name

red = '\033[31m'
green = '\033[32m'
blue = '\033[34m'
noColor = '\033[m'

losses = 0
wins = 0
empate = 0
ans = 'S'

print('=' * 9, f'{"JOKENPÔ":^6}', ('=' * 9))

while True:
    pc = ('tesoura', 'papel', 'pedra')
    pc = choice(pc)
    print('PEDRA *** PAPEL *** TESOURA ')
    user = input('\nFaça sua escolha: ').strip().lower()
    while user != 'pedra' and user != 'papel' and user != 'tesoura':
        user = input(f'{red}Opção inválida!{noColor}'
                     f'\nFaça sua escolha novamente: ').strip().lower()

    print('JO...')
    sleep(1)
    print('KEN...')
    sleep(1)
    print('PÔ!')
    print(f'\nO computador escolheu {pc}'
          f'\nE você escolheu {user}')

    if pc == 'tesoura' and user == 'papel':
        print(f'{red}Você perdeu...{noColor}')
        losses += 1
    elif pc == 'papel' and user == 'pedra':
        print(f'{red}Você perdeu...{noColor}')
        losses += 1
    elif pc == 'pedra' and user == 'tesoura':
        print(f'{red}Você perdeu...{noColor}')
        losses += 1

    elif user == 'tesoura' and pc == 'papel':
        print(f'{green}Você venceu!{noColor}')
        wins += 1
    elif user == 'papel' and pc == 'pedra':
        print(f'{green}Você venceu!{noColor}')
        wins += 1
    elif user == 'pedra' and pc == 'tesoura':
        print(f'{green}Você venceu!{noColor}')
        wins += 1
    else:
        print(f'{blue}Empatou{noColor}')
        empate += 1

    ans = input('\nDeseja jogar novamente? <S>/<N> ').strip().upper()

    while ans != 'N' and ans != 'S':
        print(f'{red}Opção inválida!{noColor}')
        ans = input('\nDeseja jogar novamente? <S>/<N> ').strip().upper()
    if ans == 'N':
        system('cls' if name == 'nt' else 'clear')
        break
    elif ans == 'S':
        system('cls' if name == 'nt' else 'clear')
        continue

print('=' * 9, f'{"Jogo encerrado":^6}', ('=' * 9))
print(f'{green}Vitórias: \t{wins}'
      f'\n{red}Derrotas: \t{losses}'
      f'\n{blue}Empates: \t{empate}{noColor}')
print('=' * 9, f'{"Volte sempre!":^6}', ('=' * 9))
