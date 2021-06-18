from datas import Data

class datas:
    def __init__(self, dia, m , a):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    def formatada(self, dia , mes , ano):
        print("Data formatada {}/{}/{}/".format(self.dia,self.mes,self.ano))


d = Data(21,11,2007)
d.formatada()
