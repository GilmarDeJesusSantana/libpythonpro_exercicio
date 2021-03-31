from libpythonproexercicio.libpythonproexercicio.spam.enviador_email import Enviador
from libpythonproexercicio.libpythonproexercicio.spam.main import EnviadorDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'gjsantana@gmail.com',
        'Curso Python Pro',
        'Confira os módulos Fantásticos'
    )
