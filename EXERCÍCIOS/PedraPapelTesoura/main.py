from random import randint
from time import sleep

itens = ("pedra","papel", "tesoura")
computador = randint(0,2)
print("Suas opções são: "
"[0] PEDRA"
"[1] PAPEL"
"[2] TESOURA")
jogador = int(input("Qual a sua jogada? "))
print("PEDRA")
sleep(1)
print("PAPEL")
sleep(1)
print("TESOURA!")
sleep(1)
print("=-"*10)
print("O computador jogou {}".format(itens[computador]))
print("O player 1 jogou {}".format(itens[jogador]))
print("=-"*10)

if computador == 0:
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("COMPUTADOR VENCE")
    else:
        print("Jogada inválida")

elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador == 2:
        print("JOGADOR VENCE")

    else:
        print("Jogada inválida")

elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print("EMPATE")
    else:
        print("Jogada inválida")