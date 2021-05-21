from fila import estacionamento

def main():
    parking = estacionamento()
    while True:

        park = str(input("Você deseja: E-Estacionar | R-Retirar Carro | S-Mostrar Estacionamento ")).strip().upper()[0]

        if park == "E":
            dadosCarro = str(input("digite a placa do veículo: "))
            parking.setDados(dadosCarro)

        elif park == "R":

            dadosCarro = str(input("digite a placa do veículo: "))
            parking.removerDadoEspecif(dadosCarro)

        elif park == "S":
            print("Ocupação: ", parking.tamanhoFila())
            print("Veículos: ", parking.getDados())

        else:
            print("Nenhuma opção selecionada.")
            return False



    if estadoPark == "S":
        print(parking.getDados())
    else:
        print("Nenhuma opção válida selecionada. Sistema encerrado!")
main()