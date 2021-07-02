# Crie um programa para o pc jogar Jokenpô com você.

from time import sleep
from random import choice
print('=' * 15, f'{"JOKENPÔ":^6}', ('=' * 15))
print('Pedra, Papel, Tesoura')
pc = ('tesoura', 'papel', 'pedra')
user = input('Faça sua escolha: ').strip().lower()
pc = choice(pc)
print('JO...')
sleep(0.5)
print('KEN...')
sleep(0.5)
print('PÔ!')
if pc == user:
    print(f'Você Venceu!')
elif pc == user:
    print('Empate')
else:
    print('Você perdeu...')
print(f'O computador escolheu {pc}')
