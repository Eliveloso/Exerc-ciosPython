
n= int(input("Qnt sequencia: "))
elemento1 = 0
elemento2 = 1
cont = 3


while cont <= n:
    elemento3 = elemento1 + elemento2
    print(" -> {}".format(elemento3),end="")
    elemento1 = elemento2
    elemento2 = elemento3
    cont = cont + 1

print("_-_-_" *10)
print("FIM")
print("_-_-_" *10)