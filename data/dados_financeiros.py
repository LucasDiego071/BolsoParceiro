class Dados_financeiros:
    def __init__(self, renda, gastos):
        self.renda = renda.renda
        self.gastos = gastos.gastos
        self.gastos_fixos = []
        self.gastos_gerais = []

    def calcular_gastos_fixos(self):
        self.total_Gastos_Fixos = 0
        for gasto in self.gastos:
            if gasto.gastos_fixo == True:
                self.gastos_fixos.append(gasto)
            else:
                continue

        for fixo in self.gastos_fixos:
            self.total_Gastos_Fixos += fixo.valor
        return self.total_Gastos_Fixos
        
    def calcular_gastos_gerais(self):
        self.total_Gastos_gerais = 0
        for gasto in self.gastos:
            if gasto.gastos_fixo == False:
                self.gastos_gerais.append(gasto)
            else:
                continue

        for fixo in self.gastos_gerais:
            self.total_Gastos_gerais += fixo.valor
        return self.total_Gastos_gerais

    def calcular_RendaTotal(self):
        rendatotal = 0
        for value in self.renda:
            rendatotal += value
        self.rendatotal = rendatotal
        return self.rendatotal

    def __str__(self) -> str:
        return f"Seu fonte de renda totaliza {self.calcular_RendaTotal()}R$ \n\
            E a quantidade de gastos no seu mês é {len(self.gastos)}"


# =========================== R E N D A ==========================
    
class Renda:
    def __init__(self):
        self.renda = []


#=========================== G A S T O (S) ==========================



class Gasto:
    def __init__(self, valor, nome) -> None:
        self.valor = valor
        self.nome = nome
        self.gasto_fixo = False

        def __str__(self):
            return self.nome

    def modificar_gastos(self, valor, nome):
        self.valor = valor
        self.nome = nome

    def __str__(self) -> str:
        return f"O valor de {self.nome} é equivalante a {self.valor}"
    
class Gasto_Fixos(Gasto):
    def __init__(self, valor, nome) -> None:
        super().__init__(valor, nome)
        self.gasto_fixo = True

class Gastos:
    def __init__(self):
        self.gastos = []

    def adicionar_Gastos(self, gasto):
        try:
            self.gastos.append(gasto)
        except:
            print(f"Não foi possivel Adicionar o 
                  {gasto.nome} a lista de Gastos")

    def remover_Gastos(self, gasto):
        try:
            self.gastos.remover(gasto)
        except:
            print(f"Não foi possivel Remover o \
                  {gasto.nome} da lista de Gastos")