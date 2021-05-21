
import math

def main():

    area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
               
    qntLitros = (area / 3)          
    

    if qntLitros <=  18:

        print ("Será necessário apenas 1 galão")
     
    elif qntLitros  > 18:
        
        qntGaloes = (qntLitros / 18 )             

        print  ("Serão necessários", math.ceil(qntGaloes) , "galões!")

main()
