from libpythonpro_exercicio.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Gilmar')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [Usuario(nome='Gilmar'), Usuario(nome='Renata')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
