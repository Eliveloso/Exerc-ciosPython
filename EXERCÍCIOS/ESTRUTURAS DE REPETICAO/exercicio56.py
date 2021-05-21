
somaidade = 0
maioridadehomem = 0
nomevelho = ""

for i in range(1,3):
    nome = input("Digite seu nome: ".strip().upper())
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite sua opção sexual[M/F]: ".strip().upper())
    print("--"*10)
    somaidade = (idade + somaidade)
    media = somaidade / 4


print("A média de idade é de {} anos".format(media))