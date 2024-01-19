class Mes:
    def __init__(self, data, usuario, dados_financeiros) -> None:
        self.data = data
        self.nome_user = usuario.nome
        self.renda = dados_financeiros.calcular_RendaTotal
        self.gastos_extras = dados_financeiros.gastos_fixos
        self.gastos_fixos = dados_financeiros.gastos_fixos
        self.valor_gasto_fixos = dados_financeiros.calcular_gastos_fixos
        self.valor_gastos_extras = dados_financeiros.calcular_gastos_gerais

    def formatar_mes (self):
        calculo01 = self.renda - self.gastos_fixos
        mes = open(f"{self.data}.txt", "x")
        mes.write(f"{self.data}\n\
                  Usuario: {self.nome_user}\n\
                    R$ {self.renda}\n\
                    Segue os gastos fixos do usuario:\n")
        for gastos in self.gastos_fixos:
            mes.write(gastos + "\n")
        mes.write(f"Restando para os gastos Extras: R$ {calculo01}\n\
                  podendo ser distribuido entre os seguintes gastos extras:\n")
        for gastos2 in self.gastos_extras:
            mes.write(gastos2 + "\n")
        mes.close()