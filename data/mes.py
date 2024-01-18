class Mes:
    def __init__(self, data, usuario, dados_financeiros) -> None:
        self.data = data
        self.nome_user = usuario.nome
        self.renda = dados_financeiros.calcular_RendaTotal
        self.gastos_extras = dados_financeiros.gastos_fixos
        self.gastos_fixos = dados_financeiros.gastos_fixos
        self.valor_gasto_fixos = dados_financeiros.calcular_gastos_fixos
        self.valor_gastos_extras = dados_financeiros.calcular_gastos_gerais
