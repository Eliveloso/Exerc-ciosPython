
n = cont = soma = 0
n = int(input("Digite um número [999 irá interromper]: "))
while n != 999:
    soma = soma + n
    cont= cont+1
    n = int(input("Digite um número [999 irá interromper]: "))

print("você digitou {} que somados dão {}".format(cont,soma))