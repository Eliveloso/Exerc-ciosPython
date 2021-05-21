
listaConcessionaria = ["Caoa Chery ", "Capital Fiat", "Mais", "Monte Carlo Peugeot", "Fiori", "Tambaí", "Cavalcanti Primo", "Promac"]
listaCarro = ["Carro A", "Carro B", "Carro C", "Carro D", "Carro F", "Carro G", "Carro H"]
listaValores = [60000.00, 80000.00, 50000.00, 75000.00, 36000.00, 48000.00, 77000.00, 150000.00]
listaParcelas = [48,60,48,60,36,40,60,60]
valorEntrada = float(20000.00)
 
def main():
    
    #Questionamento ao cliente para inserção de novos dados
    questionamento = int(input("Você gostaria de comparar mais algum carro além do que já temos? Digite 1 para sim e 2 para não: "))
    if questionamento == 1:

        while (questionamento == 1):

                        
            dadosUsuario = input("Favor digite a Concessionaria, o Carro, o Valor do carro e a quantidade de parcelas separados por vírgulas: ")
            colunaUsuario = dadosUsuario.split(",")


            listaConcessionaria.append(colunaUsuario[0])
            listaCarro.append(colunaUsuario[1])
            listaValores.append (float(colunaUsuario[2]))
            listaParcelas.append(int(colunaUsuario[3]))
            questionamento = int(input("Você gostaria de comparar mais algum carro além do que já temos? Digite 1 para sim e 2 para não: ")) 


    #adicionar as listas numa matriz (Fiz isso, pois comecei o código com lista
    #e apenas depois me dei conta da exigência do trabalho com matriz).

    matriz = []
    
    matriz.append(listaConcessionaria) #matriz [0]
    matriz.append(listaCarro)#matriz [1]
    matriz.append(listaValores)#matriz [2]
    matriz.append(listaParcelas)#matriz [3]


  #Cálculo da menor parcela
    
    menorValorParcela = (matriz[2][0] - valorEntrada) / matriz[3][0]
    
    for i in range (len(listaValores)):
        
        valorCalculado =  (matriz[2][i] - valorEntrada) / matriz[3][i]

        if valorCalculado < menorValorParcela:

            menorValorParcela = valorCalculado
            concessionaria = matriz[0][i]
            parcelasConsessionaria = matriz[3][i]

    
    print("Maria, a melhor proposta é o carro da Concessionária",concessionaria, "em" ,parcelasConsessionaria, "parcelas.")
    
           
          
    

main()

