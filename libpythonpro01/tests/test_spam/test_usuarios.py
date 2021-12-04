from libpythonpro01.spam.db import Conexao
from libpythonpro01.spam.modelos import Usuario


class Usuario:
    pass


def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    Usuario=Usuario(nome='Renzo')
    sessao.salvar(usuario)
    assert isinstance(usuario.id,int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()

def test_listar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    Usuarios=[Usuario(nome='Renzo'), Usuario(nome='Luciano')]
    for usuarios in usuarios:
        sessao.salvar(usuario)
    assert usuarios== sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
