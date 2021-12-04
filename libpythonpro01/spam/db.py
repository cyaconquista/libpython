from libpythonpro01.spam.modelos import Usuario


class Sessao:
    contador=o
    usuarios=[]
    def salvar(self, usuario):
        Sessao.contador += 1
        Usuario.id = Sessao.contador
        self.usuarios.append(usuario)
        pass

    def listar(self):
        return self.usuarios

    def roll_back(self):
        pass

    def fechar(self):
        pass


class Conexao:
    def gerar_sessao(self):
        return Sessao()

    def fechar(self):
        pass