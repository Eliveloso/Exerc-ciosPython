from datetime import date

atual = date.today().year
maior = 0
menor = 0
for nasc in range(1,8):
        nasc = int(input("Digite seu ano de nascimento: "))
        idade = atual - nasc

        if idade >= 21:
            maior = maior + 1
        else:
            menor = menor +1

print("=-" *10)
print("A quantidade de pessoas aptas a comprar bebidas alcoólicas é {}".format(maior))
print("=-" *10)
print("{} pessoas estão inaptas a comprar bebidas alcoólicas".format(menor))