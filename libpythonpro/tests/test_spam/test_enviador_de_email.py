import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'destinatario',
    ['teste@teste.com', 'estudos.josemarbrito@gmail.com', 'josemarbrito@novocloset.com']
)
def test_remetente(destinatario):
    enviador = Enviador()

    resultado = enviador.enviar(
        destinatario,
        'josemarbritosantos@gmail.com',
        'Curso Python Pro',
        'testes de baby step python pro'
    )
    assert destinatario in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'estudos.josemarbrito', 'josemarbrito.novocloset.com']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'josemarbritosantos@gmail.com',
            'Curso Python Pro',
            'testes de baby step python pro'
        )
