from time import sleep


#for i in range (10,0,-1):
    #sleep(1)
    #print(i)
#print("=-"*10)
#print("Estouro!")
#print("=-"*10)

soma = 0
cont = 0
for i in range (1,501,2):
    if i % 3 == 0:
        cont = cont + 1
        soma = soma + i
print("A soma de todos os valores somados é {}" .format(soma))
print("A quantidade de números divididos por 3 é {}" .format(cont))

print("=-"*10)
print("Soma dos múltiplos de 3")
print("=-"*10)
