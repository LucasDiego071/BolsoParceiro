class Prioridade:
    def __init__(self, nome, dados):
        self.nome = nome
        self.renda = dados.calcular_RendaTotal()
        self.gastos_fixos = dados.calcular_gastos_fixos()
        self.gastos_gerais = dados.calcular_gastos_gerais()
        self.lista_gastos_fixos = dados.gastos_fixos
        self.lista_gastos_gerais = dados.gastos_gerais

    def detalhar_distribuição(self):
        def detalhar(gasto): return print(gasto)
        detalhar_gastosgerais = list(map(detalhar, self.lista_gastos_gerais))
        detalhar_gastosfixos = list(map(detalhar, self.lista_gastos_fixos))
        calculo1 = self.renda - self.gastos_fixos

        textoa = (f"Distribuindo a renda total de: {self.renda} \
              para os gastos fixos de {self.gastos_fixos}, restam {calculo1}.\n\
            gastos fixos são {detalhar_gastosfixos}.\n")
        textob = (f"Restou {calculo1} para distribuir entre {detalhar_gastosgerais}.\n\
                  A distribuição entre esses gastos será feito de acordo com sua prioridade.")

        return textoa, textob
    
    def distrinchar_gastos(self):
        gastos = self.gastos_fixos + self.gastos_gerais
        calculo1 = self.renda - self.gastos_fixos
        print(f"Renda total: {self.renda}")
        for gastos in self.lista_gastos_fixos:
            print(f"{gastos.nome} : {gastos.valor}")
        print(f"Receita disponivel para uso gasto adicionais é: {calculo1}")
        for gastos in self.lista_gastos_gerais:
            print(f"{gastos.nome} : {gastos.valor}")
        
        return f"Valores geral: {gastos} "