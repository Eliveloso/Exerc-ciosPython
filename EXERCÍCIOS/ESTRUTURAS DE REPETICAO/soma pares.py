cont = 0
soma = 0
for i in range (0,6):
    num= int(input("Digite um número: "))
    if num % 2 == 0:
        soma += num
        cont = cont +1


print("A soma dos valores pares é {}" .format(soma))
print("A quantidade de valores pares é {}" .format(cont))