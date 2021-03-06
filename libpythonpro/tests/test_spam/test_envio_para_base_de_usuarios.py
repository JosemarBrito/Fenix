from unittest.mock import Mock

import pytest

from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    ' usuarios',
    [
        [
            Usuario(nome='Josemar', email='estudos.josemarbrito@gmail.com'),
            Usuario(nome='Guilherme', email='josemarbritosantos@gmail.com')
        ],
        [
            Usuario(nome='Josemar', email='estudos.josemarbrito@gmail.com'),
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'estudos.josemarbrito@gmail.com',
        'Curso de Python BD',
        'Os melhores curso do mercado'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Josemar', email='estudos.josemarbrito@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'josemarbritosantos@gmail.com',
        'Curso de Python BD',
        'Os melhores curso do mercado'
    )
    enviador.enviar.assert_called_once_with(
        'josemarbritosantos@gmail.com',
        'estudos.josemarbrito@gmail.com',
        'Curso de Python BD',
        'Os melhores curso do mercado'
    )
