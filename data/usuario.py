class Usuarios:
    def __init__(self) -> None:
        self.usuario = []

    def adicionar_user(self, usuario):
        try:
            self.usuario.append(usuario)
        except:
            print(f"Não foi possivel adicionar o 
                  {usuario} a lista de usuarios")

    def deletar_user(self, usuario):
        try:
            self.usuario.remove(usuario)
        except:
            print(f"Não foi possivel remover o {usuario} da lista de usuarios")

    def listar_users(self):
        for user in self.usuario:
            print(user)

    def __iter__(self):
        self.index = 0
        pass

    def __next__(self):
        if self.index < len(self.usuario):
            user = self.usuario[self.index]
            self.index += 1
            return user
        else:
            raise StopIteration
