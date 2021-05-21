
class estacionamento():

    fila = []

    def init(self):
        self.fila = []

    #devolver valores
    def getDados(self):
        return self.fila

    #inserir valores na fila
    def setDados(self, placa):
        self.fila.append(placa)

    #removervalores
    def removerDados(self, posicao):
        self.fila.pop(posicao)

    def removerDadoEspecif(self, placa):
        pos = self.fila.index(placa)
        self.removerDados(pos)
        for i in range(0, pos):
            self.setDados(self.fila[0])
            self.removerDados(0)
        return print("Retirado")


    def tamanhoFila (self):
        return len(self.fila)