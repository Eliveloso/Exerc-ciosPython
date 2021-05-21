import math
vCasa = float(input("Digite o preço da casa que pretende financiar: "))
salario = float(input("Digite o valor do seu salário: "))
fina = int(input("digite a quantidade de meses que deseja financiar: "))
minimo = salario *30 / 100

def main():

    vParcela = float(vCasa / fina)

    if vParcela > minimo:
        print("Empréstimo negado")

    elif vParcela < minimo:

        print ("Aprovado")





main()