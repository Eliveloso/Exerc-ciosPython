
preco = float(input("Valor do produto: "))
pgto = str(input("Digite a forma de pagamento(dinheiro ou cartao): "))

def main():

    if pgto == "dinheiro":

        valor = preco - (5/100 * preco)
        print("Você pagará o valor de: ",valor)

    elif pgto == "cartao":

        parcelamento = int(input("Você deseja parcelar (digite 1 para sim e 2 para não): "))

        if parcelamento == 1:

            parcela = int(input("Em quantas parcelas você deseja pagar? "))

            if parcela > 2:
                valor = preco + (20 / 100 * preco)
                print("Você pagará o valor de: ",valor)

            else:
                print("Você pagará o valor de: ",preco, "Reais")

        else:
            valor = preco - (5 / 100 * preco)
            print("Você pagará o valor de: ", valor,"Reais")

main()

