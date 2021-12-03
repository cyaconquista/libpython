import pytest as pytest

from libpythonpro01.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None
@pytest.mark.parametrize(
    'remetente',
    ['messiasdedeus@hotmail.com','manoel.pereira@grupodass.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado=enviador.enviar(
        remetente,
        'manoelmessias.pereiradedeus@gmail.com',
        'Cursos Python Pro',
        'Primeira turma guido',

    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['','manoel.pereira']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'manoelmessias.pereiradedeus@gmail.com',
            'Cursos Python Pro',
            'Primeira turma guido',

        )
    assert remetente in resultado
