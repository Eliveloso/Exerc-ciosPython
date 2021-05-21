
preco = float(input("Valor do produto: "))
pgto = str(input("Digite a forma de pagamento(dinheiro ou cartao): "))

def main():

    if pgto == "dinheiro":

        valor = preco - (5/100 * preco)
        print("Você pagará o valor de: ",valor)

    elif pgto == "cartao":

        parcelamento = str(input("Você deseja parcelar [S/N]: "))
            if parcelamento == ("S"):
                parcela = int(input("Em quantas parcelas você deseja pagar? "))
                if parcela > 2:
                    valor = preco + (20 / 100 * preco)
                print("Você pagará o valor de: ",valor)
            else:
                print("Você pagará o valor de: ",preco)

main()