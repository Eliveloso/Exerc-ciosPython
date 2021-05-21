print('--Exercício 02 para nota 01--')


def main ():
    
    n = int (input ("Digite um número para descobrir seu fatorial:  "))
    cont = n
    fatorial = 1
    print ("O cálculo fatorial de {}! é = ".format(n), end = " ")
    while cont > 0:
        print ("{}".format(cont), end = " ")
        if cont > 1:
            print(" x ", end = " ")
        else:
            print (" = ", end = " ")

        fatorial = fatorial * cont
        cont -= 1
    print(" {} ".format(fatorial))

main()
