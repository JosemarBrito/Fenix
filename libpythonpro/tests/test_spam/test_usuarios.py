from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Josemar', email='estudos.josemarbrito@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(conexao, sessao):
    usuarios = [Usuario(nome='Josemar', email='estudos.josemarbrito@gmail.com'),
                Usuario(nome='Guilherme', email='josemarbritosantos@gmail.com')
                ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
