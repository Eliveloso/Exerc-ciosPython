
class Vagas ():

    def __init__(self):
        self.dados = []

    def getFila(self):
        return self.dados

    def setDado(self, newValue):
        self.dados.append(newValue)

    def removerEspecifico(self,valor):
        pos = self.dados.index(valor)
        for i in range (0,pos +1):
            self.dados.pop(0)
            self.getFila()



filaVar = Vagas()
filaVar.setDado("Parati")
#print(filaVar.getFila())
filaVar.removerFila()
#print(filaVar.getFila())
filaVar.removerEspecifico("Uno")
print(filaVar.getFila())