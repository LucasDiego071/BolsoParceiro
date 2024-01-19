class Dados_financeiros:
    def __init__(self, renda, gastos):
        self.renda = renda.renda
        self.gastos_fixos = gastos.gastos_fixos
        self.gastos_extras = gastos.gastos_extras

    def calcular_gastos_fixos(self):
        self.total_Gastos_Fixos = 0
        for fixo in self.gastos_fixos:
            self.total_Gastos_Fixos += fixo[1]
        return self.total_Gastos_Fixos

    def calcular_gastos_extras(self):
        self.total_Gastos_gerais = 0
        for fixo in self.gastos_extras:
            self.total_Gastos_gerais += fixo[1]
        return self.total_Gastos_gerais

    def calcular_RendaTotal(self):
        rendatotal = 0
        for value in self.renda:
            rendatotal += value
        self.rendatotal = rendatotal
        return self.rendatotal

# =========================== R E N D A ==========================

class Renda:
    def __init__(self, lista):
        self.renda = lista


# =========================== G A S T O (S) ==========================

class Gastos:
    def __init__(self, lista01, lista02):
        self.gastos_fixos = lista01
        self.gastos_extras = lista02
