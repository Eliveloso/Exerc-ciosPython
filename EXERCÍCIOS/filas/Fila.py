
class Fila:

    def __init__(self):

        self.dados = []

    def getFila(self):
        return self.dados

    def setDado(self, newValue):
        self.dados.append(newValue)
        print()

    def removerFila(self):

        self.dados.pop(0)

    def removerEspecifico(self,valor):

        pos = self.dados.index(valor)
        for i in range (0,pos +1):
            self.setDado(self.dados[0])
        self.dados.pop()



filaVar = Fila()
filaVar.setDado("Parati")
#print(filaVar.getFila())
filaVar.removerFila()
#print(filaVar.getFila())
filaVar.removerEspecifico("Uno")
print(filaVar.getFila())


