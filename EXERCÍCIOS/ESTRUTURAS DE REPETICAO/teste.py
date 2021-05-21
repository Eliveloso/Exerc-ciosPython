n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro úmero: "))
opcao = 0

while opcao != 5:
    print("'[1] Somar"
        "[2] Multiplicar"
        "[3] Maior"
        "[4] Novos números"
        "[5] Sair do programa'")
    opcao = int(input("Digite sua opção:' '"))
    if opcao == 1:
        soma = n1+n2
        print("{} é a soma dos dois números digitados!".format(soma))
    elif opcao == 2:
        mult = n1 * n2
        print("{} é o produto dos dois números digitados!".format(mult))

    elif opcao == 3:

        if n1 > n2:

            print(n1,"é maior que", n2)

        elif n1 < n2:

            print(n2,"é maior que", n1)
        else:

            print("Os números são iguais")

    elif opcao == 4:
        print("Informe os números novamente!")
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro úmero: "))

    else:
        print("Opção inválida")


print("=_="*10)
print("Fim do programa")
print("=_=" * 10)