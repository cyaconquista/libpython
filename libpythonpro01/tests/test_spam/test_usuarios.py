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


class Usuario:
    pass


class Usuario:
   def __init__(self, nome):
       self.nome = nome
       self.id =None



def test_salvar_usuario():
    conexao =Conexao()
    sessao = conexao.gerar_sessao()
    Usuario=Usuario(nome='Renzo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id,int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()

def test_listar_usuario():
    conexao =Conexao()
    sessao = conexao.gerar_sessao()
    Usuarios=[Usuario(nome='Renzo'),Usuario(nome='Luciano')]
    for usuarios in usuarios:
        sessao.salvar(usuario)
    assert usuarios== sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
